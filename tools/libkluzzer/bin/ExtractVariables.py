import subprocess
import sys
import re

WithOutVars = subprocess.Popen("%s/cproto    %s" % (sys.path[0], sys.argv[1]), shell=True, stdout=subprocess.PIPE).stdout.readlines()
WithVars    = subprocess.Popen("%s/cproto -v %s" % (sys.path[0], sys.argv[1]), shell=True, stdout=subprocess.PIPE).stdout.readlines()
VarDecls = list(set(WithVars) - set(WithOutVars))

VarPairs = []

for decl in VarDecls:
	toks = decl.split()
	ignore = False
	if 'const' in toks:
		ignore = True
	elif len(toks) != 2:
		ignore = True
	elif not re.match(r"[A-Za-z0-9_]+;", toks[1]):
		ignore = True
	if ignore:
		print ("// " + decl)
	else:
		oldVar = toks[1][:-1]
		newVar = "__fuzzer_copy_" + oldVar;
		print (toks[0] + " " + newVar + ";")
		VarPairs.append((oldVar, newVar))

print ("void __fuzzer_save_ctx() {")
for ov, nv in VarPairs:
	print ("  %s = %s;" % (nv, ov))
print ("}")

print ("void __fuzzer_restore_ctx() {")
for ov, nv in VarPairs:
	print ("  %s = %s;" % (ov, nv))
print ("}")
