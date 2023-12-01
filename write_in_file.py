import os,time
def main():
    os.system("sudo mkdir -p -m 777 /test")
    os.system("ls -ld /test")

    file1 = '/test/test.txt'
    file1_content = """반갑습니다.
    안녕하세요.
    DevOps 로드맵 80% 완성중!"""
    createfile(file1,file1_content)

    if os.path.exists(file1):
        print("파일 삭제 시작")
        time.sleep(3)
        os.remove(file1)
        print("OK %s 파일이 잘 지워졌습니다." % file1)
    else:
        pass

def createfile(file,content):
    #input : file(file), str(content)
    #output : -> 파일 생성
    #function :
    #print(file,content)
    fd = open(file,'w+')
    fd.write(content)
    fd.close()
    print(open(file).read())

if __name__ == "__main__":
    main()