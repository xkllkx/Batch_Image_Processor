import cv2
import numpy as np
import pyautogui
import shutil
import os

# ----------------------------------
# 操作步驟：
# 1. 選取欲截圖範圍的左上角與右下角
# 2. 關閉圖片視窗
# 3. 確認裁切範圍
# 4. 確認欲截圖圖片之編號
# 5. 裁切完的圖片會儲存在cut_path
# ----------------------------------

def cv2_imread(file_path): # 為了讀取中文路徑
    cv2_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv2_img

print("請輸入要截圖的資料夾名稱：")
file_name = str(input())

path = f'./{file_name}/' # 欲進行檔名更改的檔案路徑
cut_path = f'./{file_name}_cut/'
# 圖片格式為jpg、png

files = os.listdir(path)

if os.path.exists(cut_path):
    shutil.rmtree(cut_path) # 避免cut_path存在

shutil.copytree(path,cut_path) # 複製資料夾

# 選取截圖範圍
print("---選取截圖範圍---")
print("請選取欲截圖範圍的左上角與右下角")

png = cv2_imread(str(path+files[0])) # 開啟第一張照片

point = 0
x0,x1 = 0,0
y0,y1 = 0,0
check = ''

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
			print("---請關閉圖片---")
			cv2.rectangle(png,(x0,y0),(x1,y1),(255,0,0),2)
		point = point+1
		cv2.circle(png, (x, y), 1, (255, 0, 0), thickness = -1)
		cv2.putText(png, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 3.0, (0,0,0), thickness = 1)
		cv2.imshow("image", png)
		cv2.waitKey(0)

monitor_w, monitor_h = pyautogui.size()
print(monitor_w, monitor_h)
print(png.shape)

resize_ratio = max(png.shape[1]/monitor_w,png.shape[0]/monitor_h,1)
print(resize_ratio)
print(png.shape[0]/resize_ratio, png.shape[1]/resize_ratio)

cv2.namedWindow("image",0)
cv2.resizeWindow('image', int(png.shape[1]/resize_ratio), int(png.shape[0]/resize_ratio))  # 初始視窗大小
# cv2.resizeWindow('image', 500, 500)  # 初始視窗大小
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
			point = 0
			x0,x1 = 0,0
			y0,y1 = 0,0
			check = ''

			png = cv2_imread(str(path+files[0]))
			cv2.destroyWindow("image")
			cv2.namedWindow("image",0)
			cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
			cv2.imshow("image", png)
			print("請選取欲截圖範圍的左上角與右下角")

	else: check==''	

n = 0
print("檔案標號確認(預設為0)(Y/N):")
file_number_check = str(input())
if file_number_check == ('N' or 'n'):
	n = str(input())
else:	pass

for i in files: # 資料夾裡面的檔案都會更換名稱
	#改名並開始裁切
	oldname = cut_path+files[n] # 指出檔案現在的路徑，[n]表示第n個檔案
	#print(oldname)
	newname = cut_path+file_name+"_"+str(n+1)+'.png' # 更改後檔案名稱
	#print(newname)

	os.rename(oldname,newname)
	print(files[n]+' >>> '+file_name+"_"+str(n+1)+'.png') # 印出原名與新名

	# opencv讀不到中文檔名，須先改名
	# 圖片格式為jpg、png
	png = cv2_imread(newname)
	png_shape = tuple(png.shape)

	if (png_shape[0] >= (y1-y0)/0.9 and png_shape[1] >= (x1-x0)/0.9):
		print("判斷裁切")
		cropped = png[y0:y1,x0:x1]  # 裁剪座標為[y0:y1, x0:x1]
		cv2.imwrite(newname, cropped)
		print(file_name+"_"+str(n+1)+'.png'+'裁切完成')
	else:
		print(file_name+"_"+str(n+1)+'.png'+'早已完成裁切')

	print("------------------------")
	n = n+1
