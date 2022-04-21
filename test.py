
#html file lists
head_list = ['html/head.html']
nav_list = ['html/nav.html']
hero_list = ['html/hero.html']
foot_list = ['html/foot.html']

#Reads the HTML files and combines them in order
filestack = [head_list[0], nav_list[0], hero_list[0],foot_list[0]]
with open('output_file.html', 'w') as outfile:
    for fname in filestack:
        with open(fname) as infile:
            outfile.write(infile.read())

#css file lists
nav_css = ['css/nav/nav1.css','css/nav/nav2.css']
hero_css = ['css/hero/hero1.css']
foot_css = ['css/foot/foot1.css']


#Reads the CSS files and combines them in order
stylestack = [nav_css[1], hero_css[0], foot_css[0]]
with open('output.css', 'w') as outfile:
    for fname in stylestack:
        with open(fname) as infile:
            outfile.write(infile.read())


#javascript file lists 


#Reads the javascript file and combines them in order


