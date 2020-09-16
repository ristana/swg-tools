import sys
import string

#initial variables

actionName=""

line_1a = "public int "
line_1b = "(obj_id self, obj_id target, String params, float defaultTime) throws InterruptedException"

line_2 = "{"
line_3a = "    if (!combatStandardAction(\""
line_3b = "\", self, target, params, \"\", \"\"))"

line_4 = "    {"
line_5 = "        return SCRIPT_OVERRIDE;"
line_6 = "    }"
line_7 = "    return SCRIPT_CONTINUE;"
line_8 = "}"

lb = "\n"

# Example Entry
#    public int carbineer_return_fire_reac(obj_id self, obj_id target, String params, float defaultTime) throws InterruptedException
#    {
#        if (!combatStandardAction("carbineer_return_fire_reac", self, target, params, "", ""))
#        {
#            return SCRIPT_OVERRIDE;
#        }
#        return SCRIPT_CONTINUE;
#    }

f2 = open("out.txt", "a")

#read input file
with open('in.txt') as f:
	content = f.readlines()
	content = [x.strip() for x in content] 
	for line in content:
		actionName = line

		#combine lines with variable
		line_1 = line_1a + actionName + line_1b
		line_3 = line_3a + actionName + line_3b
		
		#format stuff for output
		newEntry = line_1 + lb + line_2 + lb + line_3 + lb + line_4 + lb + line_5 + lb + line_6 + lb + line_7 + lb + line_8 + lb
		
		#write to file
		f2.write(newEntry)

#close file
f2.close