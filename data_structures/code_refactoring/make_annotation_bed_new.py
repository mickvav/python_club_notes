from sys import argv
import csv
from collections import defaultdict, namedtuple

##sequence-region NZ_CP008708.1 1 8731
##sequence-region NZ_CP008709.1 1 1967
#NZ_CP008706.1  Prodigal:002006 CDS 1   1398    .   +   0   ID=LCHADHJN_00001;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:GCF_000963815.1_ASM96381v1_translated_cds.faa:lcl|NZ_CP008706.1_prot_WP_000964768.1_1;locus_tag=LCHADHJN_00001;product=[gene%3DdnaA] [locus_tag%3DABUW_RS00005] [protein%3Dchromosomal replication initiator protein DnaA] [protein_id%3DWP_000964768.1] [location%3D95..1492][gbkey%3DCDS]
#NZ_CP008706.1  Prodigal:002006 CDS 1496    2644    .   +   0   ID=LCHADHJN_00002;inf
#['NZ_CP008706.1', 'Prodigal:002006', 'CDS', '187619', '187750', '.', '+', '0', 'ID=LCHADHJN_00164;inference=ab initio prediction:Prodigal:002006;locus_tag=LCHADHJN_00164;product=hypothetical protein']

gff = open(argv[1], "r")
bed = open(argv[1]+".fin.bed", "w")
def get_features(file):
    Feature = namedtuple("Feature", "chrom start stop ori entry_type locus_tag1 old_locus1 product1 locus_tag2 old_locus2 product2")
    feature_dict = defaultdict(namedtuple)
    locus_list = []
    dna_length = {}

    for line in file:
        line = line.strip().split("\t")
        if line[0][0] == ">":
            break
        if line[0][0] == "#":
            seq = line[0].split(" ")
            if seq[0] == "##sequence-region":
                dna_length[seq[1]]=int(seq[3])
        else:
            chrom = line[0]
            start = int(line[3])-1
            stop = int(line[4])
            ori = line[6]
            descr = line[8].split(";")
            locus_tag = descr[0].split("=")[1]
            entry_type = line[2]
            old_locus = "no"
            product = "no"
            if entry_type == "CDS":
                prod_desc = descr[3].split(" ")
                if len(prod_desc) > 2:
                    for i in prod_desc:
                        if "locus_tag" in i:
                            old_locus = i.split("%")[1][2:-1]
                        if "product=" in i:
                            
                            product = i.split("=")[1]
                            if product[0] == "[":
                                product = product.split("%")[1][2:-1]     
            cur_feature = Feature(chrom,start, stop, ori, entry_type, locus_tag, old_locus, product, locus_tag, old_locus, product)
            locus_list.append(locus_tag)
            feature_dict[locus_tag] = cur_feature
    return dna_length, feature_dict, locus_list
def add_intergenic (feature_dict,dict_size, locus_list):
    Feature = namedtuple("Feature", "chrom start stop ori entry_type locus_tag1 old_locus1 product1 locus_tag2 old_locus2 product2")
    feature_dict_inter = defaultdict(namedtuple)
    first_locus = locus_list[0]
    for i in range(len(locus_list)):
        if i == 0:
            feature_dict_inter[locus_list[i]] = feature_dict[locus_list[i]]
        elif feature_dict[locus_list[i]].chrom == feature_dict[locus_list[i-1]].chrom:
            if feature_dict[locus_list[i]].start > feature_dict[locus_list[i-1]].stop:
                inter_locus = locus_list[i-1]+"_"+locus_list[i]
                inter_feature = Feature(feature_dict[locus_list[i]].chrom, feature_dict[locus_list[i-1]].stop, feature_dict[locus_list[i]].start, \
                        feature_dict[locus_list[i-1]].ori+feature_dict[locus_list[i]].ori, "intergenic", feature_dict[locus_list[i-1]].locus_tag1,feature_dict[locus_list[i-1]].old_locus1,feature_dict[locus_list[i-1]].product1, feature_dict[locus_list[i]].locus_tag1, feature_dict[locus_list[i]].old_locus1,feature_dict[locus_list[i]].product1)
                feature_dict_inter[inter_locus] = inter_feature
            feature_dict_inter[locus_list[i]] = feature_dict[locus_list[i]]
        else:
            #new chromosome starts, we need to close the previous one and strat the new one
            #prev chrom
            if feature_dict[locus_list[i-1]].stop < dict_size[feature_dict[locus_list[i-1]].chrom]:
                inter_locus = locus_list[i-1]+"_end"
                inter_feature = Feature(feature_dict[locus_list[i-1]].chrom, feature_dict[locus_list[i-1]].stop, dict_size[feature_dict[locus_list[i-1]].chrom], \
                        feature_dict[locus_list[i-1]].ori+feature_dict[first_locus].ori, \
                        "intergenic", feature_dict[locus_list[i-1]].locus_tag1,feature_dict[locus_list[i-1]].old_locus1,feature_dict[locus_list[i-1]].product1, \
                        feature_dict[first_locus].locus_tag1, feature_dict[first_locus].old_locus1,feature_dict[first_locus].product1)
                feature_dict_inter[inter_locus] = inter_feature
            if feature_dict[first_locus].start >0:
                inter_locus = "start_"+first_locus
                inter_feature = Feature(feature_dict[locus_list[i-1]].chrom, 0, feature_dict[first_locus].start, feature_dict[locus_list[i-1]].ori+\
                        feature_dict[first_locus].ori,"intergenic", feature_dict[locus_list[i-1]].locus_tag1,feature_dict[locus_list[i-1]].old_locus1,\
                        feature_dict[locus_list[i-1]].product1, feature_dict[first_locus].locus_tag1,feature_dict[first_locus].old_locus1,\
                        feature_dict[first_locus].product1)
                feature_dict_inter[inter_locus] = inter_feature


            first_locus = locus_list[i]
            feature_dict_inter[locus_list[i]] = feature_dict[locus_list[i]]
    if feature_dict[locus_list[i]].stop < dict_size[feature_dict[locus_list[i]].chrom]:
        inter_locus = locus_list[i]+"_end"
        inter_feature = Feature(feature_dict[locus_list[i]].chrom, feature_dict[locus_list[i]].stop, dict_size[feature_dict[locus_list[i]].chrom], \
                        feature_dict[locus_list[i]].ori+feature_dict[first_locus].ori, "intergenic", feature_dict[locus_list[i]].locus_tag1, \
                        feature_dict[locus_list[i]].old_locus1,feature_dict[locus_list[i]].product1, \
                        feature_dict[first_locus].locus_tag1, feature_dict[first_locus].old_locus1,feature_dict[first_locus].product1)
        feature_dict_inter[inter_locus] = inter_feature
    if feature_dict[first_locus].start >0:
        inter_locus = "start_"+first_locus
        inter_feature = Feature(feature_dict[locus_list[i-1]].chrom, 0, feature_dict[first_locus].start, feature_dict[locus_list[i-1]].ori+\
                        feature_dict[first_locus].ori,"intergenic", feature_dict[locus_list[i-1]].locus_tag1,feature_dict[locus_list[i-1]].old_locus1,\
                        feature_dict[locus_list[i-1]].product1, feature_dict[first_locus].locus_tag1,feature_dict[first_locus].old_locus1,\
                        feature_dict[first_locus].product1)
        feature_dict_inter[inter_locus] = inter_feature
    return feature_dict_inter


size_dict, feat_dict, locus_list = get_features(gff)

writer = csv.writer(bed, delimiter='\t')
final_dict = add_intergenic(feat_dict,size_dict,locus_list)

writer.writerow(final_dict[locus_list[0]]._fields)  # header
for feature in final_dict:
    writer.writerow(final_dict[feature])
    
 
