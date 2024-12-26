#!/usr/bin/env python3

import unittest
import coverage
from make_annotation_bed_new import Feature, extractFeature

class TestFeature(unittest.TestCase):
    def test_extractFeature(self):
        line = 'NZ_CP008706.1	Prodigal:002006	CDS	1	1398	.	+	0	ID=LCHADHJN_00001;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:GCF_000963815.1_ASM96381v1_translated_cds.faa:lcl|NZ_CP008706.1_prot_WP_000964768.1_1;locus_tag=LCHADHJN_00001;product=[gene%3DdnaA] [locus_tag%3DABUW_RS00005] [protein%3Dchromosomal replication initiator protein DnaA] [protein_id%3DWP_000964768.1] [location%3D95..1492][gbkey%3DCDS]'
        line = line.strip().split("\t")
        locus_tag, feature = extractFeature(Feature, line)
        self.assertEqual(feature.chrom, "NZ_CP008706.1")
        self.assertEqual(feature.start, 0)
        self.assertEqual(feature.stop, 1398)
        self.assertEqual(feature.ori, "+")
        self.assertEqual(feature.entry_type, "CDS")
        self.assertEqual(feature.locus_tag1, "LCHADHJN_00001")
        self.assertEqual(feature.old_locus1, "ABUW_RS00005")
        self.assertEqual(feature.product1, "dnaA")
        self.assertEqual(feature.locus_tag2, "LCHADHJN_00001")
        self.assertEqual(feature.old_locus2, "ABUW_RS00005")
        self.assertEqual(feature.product2, "dnaA")
        self.assertEqual(locus_tag, "LCHADHJN_00001")

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.xml_report(outfile='coverage.xml')