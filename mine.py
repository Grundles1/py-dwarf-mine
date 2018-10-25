import re  # for spliting DIEs
import pdb

# regular expression to capture DIEs
DIE_re = r"<([0-9a-f]*)><([0-9a-f]*)>:\s+Abbrev\s+Number:\s+(\d+)\s+\(DW_TAG_(.*)\)\n(\s+<([0-9a-f]*)>\s+DW_AT_([^ ]*)\s+:(.*)\n)*"

if __name__=="__main__":
	with open("hello.dwarf.info") as f:
		lines = f.readlines()
	DIEs = re.split(DIE_re, '\n'.join(lines), re.MULTILINE)
	pdb.set_trace()
	print(DIEs[1])