import webbrowser

link = input("Link Cần Rút Gọn Là: ")
APIlink = "https://web1s.com/st?token=da97ea36-b611-4cf4-9633-4f7b5a5d67cb&url="
chuoilink = str(APIlink) + str(link)

webbrowser.open(chuoilink)
