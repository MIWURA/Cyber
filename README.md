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
