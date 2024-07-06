import cv2
import numpy as np
import os

print("請輸入要截圖的資料夾名稱：")
file_name = str(input())

path='D://Users//xkllkx//Desktop//all_program//photo_cut//'+file_name+'//' #檔名更改的檔案路徑
#路徑不能包含中文
#圖片是否在該路徑下，確保路徑沒有問題。
#路徑中單斜杠'\'替換成雙斜杠'\\'或'//'或'/'

files=os.listdir(path)
#print('files') #印出讀取到的檔名稱



#選取截圖範圍
print("---選取截圖範圍---")
print("請選取欲截圖範圍的左上角與右下角")

png = cv2.imread(str(path+files[0]))

point=0
x0=0
x1=0
y0=0
y1=0
check=''

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
	global point,x0,x1,y0,y1
	if event == cv2.EVENT_LBUTTONDOWN:
		xy = "%d,%d" % (x, y)
		print (xy)
		if point == 0:
			x0=x
			y0=y
			print("已選取1個點,還剩1個點")
		else:
			x1=x
			y1=y
			print("已選取2個點,完成選取")
			cv2.rectangle(png,(x0,y0),(x1,y1),(255,0,0),2)
		point = point+1
		cv2.circle(png, (x, y), 1, (255, 0, 0), thickness = -1)
		cv2.putText(png, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
					1.0, (0,0,0), thickness = 1)
		cv2.imshow("image", png)
		cv2.waitKey(0)

cv2.namedWindow("image",0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", png)

while(check != ('Y' or 'y')):
	if point!=2 and check=='':
		try:
			cv2.waitKey(100)
		except Exception:
			cv2.destroyWindow("image")
			break
	elif point == 2:

		print("裁切範圍確認(Y/N):")
		check = str(input())
		if (check == 'Y' or check == 'y') :
			print("---改名並開始裁切---")
			break
		else:
			print("---返回並重新選擇範圍---")
			check=''
			point=0
			x0=0
			x1=0
			y0=0
			y1=0
			png = cv2.imread(str(path+files[0]))
			cv2.destroyWindow("image")
			cv2.namedWindow("image",0)
			cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
			cv2.imshow("image", png)
			print("請選取欲截圖範圍的左上角與右下角")

	else: check==''	



n=0 #設定初始值
print("檔案標號確認(預設為0)(Y/N):")
file_number_check = str(input())
if file_number_check == ('N' or 'n'):
	n = str(input())
else:	pass

#opencv讀不到中文檔名，所以須先改名
#圖片格式要對，例如：jpg、png

for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	
	#改名並開始裁切
	oldname=path+files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
	#print(oldname)
	newname=path+file_name+"_"+str(n+1)+'.png'
	#print(newname)

	os.rename(oldname,newname)
	print(files[n]+' >>> '+file_name+"_"+str(n+1)+'.png') #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應

	#opencv讀不到中文檔名，所以須先改名
	#圖片格式要對，例如：jpg、png
	png = cv2.imread(newname)

	#y0=179
	#y1=904
	#x0=130
	#x1=1406
	#print(png.shape) # (1157, 3840, 3)
	png_shape = tuple(png.shape)

	if (png_shape[0] >= (y1-y0)/0.9 and png_shape[1] >= (x1-x0)/0.9):
		print("判斷裁切")
		cropped = png[y0:y1,x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
		cv2.imwrite(newname, cropped)
		print(file_name+"_"+str(n+1)+'.png'+'裁切完成')	
	else:
		print(file_name+"_"+str(n+1)+'.png'+'早已完成裁切')

	print("------------------------")
	n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束

	#待更新:
	#重複檔名會出錯
	#檔名不能有中文
