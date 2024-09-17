import re
import csv



# dictionary containing the mapping of the argument to what the fields in
# the AsciiDoc table should be
variable_mapping = {}
variable_mapping['imm12'] = 'imm[11:0]'
variable_mapping['rs1'] = 'rs1'
variable_mapping['rs2'] = 'rs2'
variable_mapping['rd'] = 'rd'
variable_mapping['imm20'] = 'imm[31:12]'
variable_mapping['bimm12hi'] = 'imm[12|10:5]'
variable_mapping['bimm12lo'] = 'imm[4:1|11]'
variable_mapping['imm12hi'] = 'imm[11:5]'
variable_mapping['imm12lo'] = 'imm[4:0]'
variable_mapping['jimm20'] = 'imm[20|10:1|11|19:12]'
variable_mapping['zimm'] = 'uimm'
variable_mapping['shamtw'] = 'shamt'
variable_mapping['shamtd'] = 'shamt'
variable_mapping['shamtq'] = 'shamt'
variable_mapping['rd_p'] = "rd"
variable_mapping['rs1_p'] = "rs1"
variable_mapping['rs2_p'] = "rs2"
variable_mapping['rd_rs1_n0'] = 'rd/rs!=0'
variable_mapping['rd_rs1_p'] = 'rs1/rs2'
variable_mapping['c_rs2'] = 'rs2'
variable_mapping['c_rs2_n0'] = 'rs2!=0'
variable_mapping['rd_n0'] = 'rd!=0'
variable_mapping['rs1_n0'] = 'rs1!=0'
variable_mapping['c_rs1_n0'] = 'rs1!=0'
variable_mapping['rd_rs1'] = 'rd/rs1'
variable_mapping['zimm6hi'] = 'uimm[5]'
variable_mapping['zimm6lo'] = 'uimm[4:0]'
variable_mapping['c_nzuimm10'] = "nzuimm[5:4|9:6|2|3]"
variable_mapping['c_uimm7lo'] = 'uimm[2|6]'
variable_mapping['c_uimm7hi'] = 'uimm[5:3]'
variable_mapping['c_uimm8lo'] = 'uimm[7:6]'
variable_mapping['c_uimm8hi'] = 'uimm[5:3]'
variable_mapping['c_uimm9lo'] = 'uimm[7:6]'
variable_mapping['c_uimm9hi'] = 'uimm[5:4|8]'
variable_mapping['c_nzimm6lo'] = 'nzimm[4:0]'
variable_mapping['c_nzimm6hi'] = 'nzimm[5]'
variable_mapping['c_imm6lo'] = 'imm[4:0]'
variable_mapping['c_imm6hi'] = 'imm[5]'
variable_mapping['c_nzimm10hi'] = 'nzimm[9]'
variable_mapping['c_nzimm10lo'] = 'nzimm[4|6|8:7|5]'
variable_mapping['c_nzimm18hi'] = 'nzimm[17]'
variable_mapping['c_nzimm18lo'] = 'nzimm[16:12]'
variable_mapping['c_imm12'] = 'imm[11|4|9:8|10|6|7|3:1|5]'
variable_mapping['c_bimm9lo'] = 'imm[7:6|2:1|5]'
variable_mapping['c_bimm9hi'] = 'imm[8|4:3]'
variable_mapping['c_nzuimm5'] = 'nzuimm[4:0]'
variable_mapping['c_nzuimm6lo'] = 'nzuimm[4:0]'
variable_mapping['c_nzuimm6hi'] = 'nzuimm[5]'
variable_mapping['c_uimm8splo'] = 'uimm[4:2|7:6]'
variable_mapping['c_uimm8sphi'] = 'uimm[5]'
variable_mapping['c_uimm8sp_s'] = 'uimm[5:2|7:6]'
variable_mapping['c_uimm10splo'] = 'uimm[4|9:6]'
variable_mapping['c_uimm10sphi'] = 'uimm[5]'
variable_mapping['c_uimm9splo'] = 'uimm[4:3|8:6]'
variable_mapping['c_uimm9sphi'] = 'uimm[5]'
variable_mapping['c_uimm10sp_s'] = 'uimm[5:4|9:6]'
variable_mapping['c_uimm9sp_s'] = 'uimm[5:3|8:6]'


#0 is the number that represents ambiguous results on here

left_shift = {}
left_shift['imm20'] = 0  #JAL = 1, LUI,AUIPC = 20
left_shift['bimm12hi'] = 1
