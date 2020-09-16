import sys
import string

if len(sys.argv) <= 1:
    print("Please provide 2 arguements \n example syntax: iconMapping.py ui_new_icons_temp6 base06")
    exit(1)

#take input vars
sourceKey = str(sys.argv[1])
nameKey = str(sys.argv[2])

#shouldnt happen but if empty set names
if not nameKey:
	nameKey = "noName"

if not sourceKey:
	sourceKey="noTexture"

#starting X/Y coords
X1 = 17
X2 = 64
Y1 = 17
Y2 = 64

#format stuff for output
format_start  = "				<ImageStyle"
format_name   = "					Name="
format_source = "					Source="
format_coords = "					SourceRect="
format_end    = "				/>"

#add quotes to the name
sourceValue = "'" + sourceKey + "'"

#				<ImageStyle
#					Name='costume_hutt_female'
#					Source='ui_new_icons_temp10'
#					SourceRect='305,448,353,496'
#				/>

# add a newline to top of output for easier pasting
print ("")

#start of loop
for y in range(0,10):
	if y > 0:
		Y1 = Y1 + 48
		Y2 = Y2 + 48
	X1 = 17
	X2 = 64
	for x in range(0,10): 
		if x > 0:
			X1 = X1 + 48
			X2 = X2 + 48
		#grab coordinates and the name
		coordinates = "'" + str(X1) + "," + str(Y1) + "," + str(X2) + "," + str(Y2) + "'"
		nameValue = "'" + nameKey + "_" + str(y) + "_" + str(x) + "'"
		
		#add in formatting
		fully_formatted = format_start + "\n" + format_name + nameValue + "\n" + format_source + sourceValue + "\n" + format_coords + coordinates + "\n" + format_end
		
		#output string
		print(fully_formatted)