#!/usr/bin/env python
from sys import argv, exit
import pegasusio as io
import scanpy as sc
if len(argv) != 4:
	print("Usage: python merge_data_across_batches.py input_sheet.csv output_barcodes.tsv ngene")
	exit(-1)
sheet=pg.read_csv(argv[2])
for batch in sheet.batch:
    
    data = [sc.read_h5ad(h5) for h5 in sheet.RNA[sheet.batch==batch]]
    [exec("data[i].obs_names=data[i].obs_names+'-'"+str(i)) for i in range(len(data))]

    [sc.pp.filter_cells(min_genes=int(argv[3])) for h5 in data]
    data=sc.concat(data)
    data=io.MultimodalData(data)
    data.write_output(batch+"merged.h5")

    with open(batch+"output_barcodes.tsv", "w") as fout:
        fout.write('\n'.join(data.obs_names) + '\n')
