from collections import  deque

class FileNode :
    def  __init__(self, name, is_file=False):
        self.name=name
        self.is_file=is_file
        self.children=[]

    def add_child(self,node):
        self.children.append(node)

## BUild a tree
root = FileNode("Root")
doc=FileNode("Dcument")
music=FileNode("Music")
pic=FileNode("Picture")

song=FileNode("song.mp3",is_file=True)
resume=FileNode("resume.pdf",is_file=True)
photo=FileNode("Sachinpic.png",is_file=True)
report=FileNode("Resport.pdf",is_file=True)
vacation=FileNode("Vacation.jpg",is_file=True)
kk_songs=FileNode("Tere Liye.mp3",is_file=True)

project=FileNode("Project")
doc.add_child(resume)
doc.add_child(report)

pic.add_child(photo)
pic.add_child(vacation)
indian_song=FileNode("Indian Songs")
indian_song.add_child(kk_songs)
music.add_child(indian_song)
music.add_child(song)

## Now add add main folders in root folder.
root.add_child(doc)
root.add_child(music)
root.add_child(pic)

def post_ordered(node, indent=""):
    # First traverse to children of current node and print it till end by recursivelly calling this method.
    for child in node.children:
        post_ordered(child, indent+"  ")
        # print file/folder from last
        print(f"{indent} Deleting {"📄 " if child.is_file else "📁 "}{child.name}")

post_ordered(root)


