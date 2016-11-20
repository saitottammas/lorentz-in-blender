import bpy

#ウィンドウ上のオブジェクトを一度削除
for item in bpy.context.scene.objects:
    if item.type == 'MESH':
        bpy.context.scene.objects.unlink(item)
for item in bpy.data.objects:
    if item.type == 'MESH':
         bpy.data.objects.remove(item)
for item in bpy.data.meshes:
     bpy.data.meshes.remove(item)
for item in bpy.data.materials:
     bpy.data.materials.remove(item)

#ローレンツの微分方程式を３つ定義
def fx(xx,yy,zz):
 q=-s*xx+s*yy
 return q
 
def fy(xx,yy,zz):
 q=r*xx-yy-xx*zz
 return q

def fz(xx,yy,zz):
 q=-b*zz+xx*yy
 return q
 
#初期定数設定
s=10
b=8/3
r=28
dt=0.01 #微分間隔　0.1にするとぼんやりした画像に

tmax=1000 #繰り返し回数　最初は100ぐらいで試すほうが無難
X=Y=Z=1.0
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 1, size = 0.2, location = (X,Y,Z))

#ルンゲクッタ法による微分方程式の解の近似値を求めて描画
for i in range(0,tmax):
 d1x=dt*fx(X,Y,Z)
 d1y=dt*fy(X,Y,Z)
 d1z=dt*fz(X,Y,Z) 
 d2x=dt*fx(X+d1x*0.5,Y+d1y*0.5,Z+d1z*0.5)
 d2y=dt*fy(X+d1x*0.5,Y+d1y*0.5,Z+d1z*0.5)
 d2z=dt*fz(X+d1x*0.5,Y+d1y*0.5,Z+d1z*0.5) 
 d3x=dt*fx(X+d2x*0.5,Y+d2y*0.5,Z+d2z*0.5)
 d3y=dt*fy(X+d2x*0.5,Y+d2y*0.5,Z+d2z*0.5)
 d3z=dt*fz(X+d2x*0.5,Y+d2y*0.5,Z+d2z*0.5) 
 d4x=dt*fx(X+d3x,Y+d3y,Z+d3z) 
 d4y=dt*fy(X+d3x,Y+d3y,Z+d3z) 
 d4z=dt*fz(X+d3x,Y+d3y,Z+d3z) 
 X=X+(d1x+2*d2x+2*d3x+d4x)/6.0
 Y=Y+(d1y+2*d2y+2*d3y+d4y)/6.0
 Z=Z+(d1z+2*d2z+2*d3z+d4z)/6.0
 bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 1, size = 0.2, location = (X, Y, Z))
