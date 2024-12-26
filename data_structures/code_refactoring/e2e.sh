#!/bin/bash
#
python3 ./make_annotation_bed_new.py GCF_000963815.1_ASM96381v1_dnaA.gff
diff GCF_000963815.1_ASM96381v1_dnaA.gff.fin.bed GCF_000963815.1_ASM96381v1_dnaA.gff.fin.bed.expected
