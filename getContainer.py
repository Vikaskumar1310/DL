import os
skc = 0
krc = 0
file ="cat_and_dog_cnn.py"
	

with open("/root/task/Code/" + file, 'r') as reader:
     for line in reader:
            sk = "sklearn"
            kr = "keras"
            if sk in line:
                skc += 1
            if kr in line:
                krc += 1
cname = ""

if krc > skc:
    cname = "dl:1"
else:
    cname = "ml:1"

print("kr " + str(krc)  + " sk " + str(skc) + " cname " + str(cname))
command = """if sudo docker ps | grep ml
then
sudo docker rm -f ml
fi
sudo docker run -dit -v /root/task/cnn_dataset/:/Dataset/ --name mlos {} bash"""

os.system(command.format(cname))

