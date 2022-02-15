# Cyber

How to Run Baby Ransomware

1. run file baby_ransomware.py เลือก mode 1 จะทำการรันเข้ารหัสไฟล์ที่ระบุไว้ใน baby_ransomware_test.py แล้วสร้างไฟล์ localkey
2. เลือก mode 2 , โปรแกรมจะถามว่า: Paste RSA Private Key and Press Enter:
3. copy private key ในไฟล์ RSAKey.txt (PRIVATE KEY: "copyในนี้ทั้งหมด") past in command line click Enter
4. program run successfully

//ตอนนี้งานรันได้ตามคำสั่งแล้ว ตามที่เข้าใจนะ น่าจะ input ข้อมูล และแสดงข้อมูลตามนี้แหละ
โปรแกรมจะไม่ถามชื่อไฟล์ที่จะเข้ารหัส หรือถอดรหัสนะ เพราะโจทย์สั่งไว้ว่าให้ "ระบุชื่อไฟล์เป้าหมายที่แน่นอนในโปรแกรม" ระบุไปแล้วใน baby_ransomware_test.py
ไฟล์ localkey ถูกเข้ารหัสด้วย rsa public key จึงเปิดอ่านไม่ได้
ในนี้ใส่ RSA ไปในไฟล์ baby_ransomware_test.py คือสร้างแล้วนะ รู้ pv key และ pb key แล้ว(ค่าไม่เปลี่ยนทุกครั้งที่รัน รันครั้งเดียวแล้วเอาไปใช้ได้เลย) เลยเอามาวางไว้เลยนะ

//ถ้างาน run ตรงไหนผิด ก็แก้ได้เลยนะ 

<!-- ABOUT THE PROJECT -->
## Run The Project Step by Step
<li>install pip v22.0.3 : https://pip.pypa.io/en/stable/installation/ </li>

<li> step 1 : pip install pycryptodome</li> 
<img width="500" alt="Screenshot 2022-02-15 141132" src="https://user-images.githubusercontent.com/96409589/154011927-59558a78-1547-4db0-bd44-5fd77183546d.png">

<li> step 2 : run file baby_ransomware.py choose Mode 1 : python3 baby_ransomware.py </li>
<img width="623" alt="image" src="https://user-images.githubusercontent.com/96409589/154012427-c00855ef-5cac-446f-ab0f-fd125ef235ad.png">
<li> ไฟล์รูปและtext ถูกเข้ารหัส ไฟล์ localkey ถูกสร้าง </li>
<img width="173" alt="image" src="https://user-images.githubusercontent.com/96409589/154013017-0abe6ba4-fef0-4034-90d5-8912ed8f9b63.png">


<li> step 3 : run file baby_ransomware.py choose Mode 2 </li>
<img width="389" alt="image" src="https://user-images.githubusercontent.com/96409589/154012733-15711ba6-4f4d-484c-bfae-98540caeab0d.png">

<li> step 4 : copy pv key in file RSAKey.txt past in cmd </li>
<img width="938" alt="image" src="https://user-images.githubusercontent.com/96409589/154014984-d6580806-2ef6-4e4b-a159-526d9460c3fc.png">

<li> step 5 : click Enter </li>
<img width="581" alt="image" src="https://user-images.githubusercontent.com/96409589/154015302-97d82b51-3e19-4e0a-82d3-7577550dafcc.png">
<li> ไฟล์รูปและtext ถูกถอดรหัสกลับมาเหมือนเดิม </li>
<img width="143" alt="image" src="https://user-images.githubusercontent.com/96409589/154015389-c3b94e80-8fe6-439b-b645-cbffc6ee4ee0.png">

