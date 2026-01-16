

# 📚 Student Task Management System

A full‑stack application designed to **streamline communication between teachers and students**.  
Teachers can register students, assign tasks, and track progress. Students can log in, view tasks, and update their status in real time.

---

## 📝 Problem Statement

Managing student tasks manually can be inefficient and error‑prone.  
The **Student Task Management System** solves this by providing a centralized platform where:

- 👨‍🏫 **Teachers** can add students, assign tasks, and monitor progress.  
- 🎓 **Students** can log in securely, view assigned tasks, and update their status (`PENDING`, `COMPLETED`, `NOTCOMPLETED`).  

This ensures **better accountability, transparency, and productivity** in the learning process.

---

## ⚙️ Features & Workflow

### 👨‍🏫 Teacher Features
- Register new students with details (username, email, name).  
- Assign tasks with descriptions and deadlines.  
- Manage tasks (update, edit, delete).  
- View all tasks and filter by status or student.  
- View all registered students.  

### 🎓 Student Features
- Secure login with credentials.  
- View assigned tasks.  
- Filter tasks by status or teacher.  
- Update task status (`COMPLETED`, `PENDING`, `NOTCOMPLETED`).  

### 🔑 Authentication
- Secure login via `/auth/token`.  
- OAuth2 with password grant.  
- Access token required for protected routes.  

---

## 🔄 Use Case Diagram

<?plantuml 1.2026.1beta2?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" data-diagram-type="DESCRIPTION" height="508px" preserveAspectRatio="none" style="width:402px;height:508px;background:#FFFFFF;" version="1.1" viewBox="0 0 402 508" width="402px" zoomAndPan="magnify"><defs/><g><!--cluster Student Task Management System--><g class="cluster" data-qualified-name="Student Task Management System" data-source-line="6" id="ent0004"><rect fill="none" height="495" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:1;" width="290.1" x="106.68" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="275.5498" x="113.9551" y="21.9951">Student Task Management System</text></g><!--entity UC1--><g class="entity" data-qualified-name="Student Task Management System.UC1" data-source-line="7" id="ent0005"><ellipse cx="251.7308" cy="188.9962" fill="#F1F1F1" rx="74.6308" ry="17.3262" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="117.8311" x="192.8152" y="193.6446">Register Student</text></g><!--entity UC2--><g class="entity" data-qualified-name="Student Task Management System.UC2" data-source-line="8" id="ent0006"><ellipse cx="251.734" cy="121.9968" fill="#F1F1F1" rx="61.084" ry="14.6168" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="82.7969" x="210.3356" y="126.6452">Assign Task</text></g><!--entity UC3--><g class="entity" data-qualified-name="Student Task Management System.UC3" data-source-line="9" id="ent0007"><ellipse cx="251.7307" cy="57.0041" fill="#F1F1F1" rx="64.6707" ry="15.3341" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92.5928" x="205.4344" y="61.6526">Manage Task</text></g><!--entity UC4--><g class="entity" data-qualified-name="Student Task Management System.UC4" data-source-line="10" id="ent0008"><ellipse cx="251.7276" cy="322.0036" fill="#F1F1F1" rx="58.0176" ry="14.5236" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="77.8066" x="212.8243" y="326.6521">View Tasks</text></g><!--entity UC5--><g class="entity" data-qualified-name="Student Task Management System.UC5" data-source-line="11" id="ent0009"><ellipse cx="251.7271" cy="256.9994" fill="#F1F1F1" rx="67.6471" ry="15.9294" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="100.3857" x="201.5342" y="261.6479">View Students</text></g><!--entity UC6--><g class="entity" data-qualified-name="Student Task Management System.UC6" data-source-line="12" id="ent0010"><ellipse cx="251.7261" cy="464.9992" fill="#F1F1F1" rx="93.0461" ry="21.0092" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="160.6035" x="171.4243" y="469.6477">Login &amp; Authentication</text></g><!--entity UC7--><g class="entity" data-qualified-name="Student Task Management System.UC7" data-source-line="13" id="ent0011"><ellipse cx="251.7315" cy="389.9983" fill="#F1F1F1" rx="82.5915" ry="18.9183" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="136.7461" x="183.3584" y="394.6467">Update Task Status</text></g><!--entity T--><g class="entity" data-qualified-name="T" data-source-line="3" id="ent0002"><ellipse cx="34.3418" cy="159.35" fill="#F1F1F1" rx="8" ry="8" style="stroke:#181818;stroke-width:0.5;"/><path d="M34.3418,167.35 L34.3418,194.35 M21.3418,175.35 L47.3418,175.35 M34.3418,194.35 L21.3418,209.35 M34.3418,194.35 L47.3418,209.35" fill="none" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56.6836" x="6" y="223.8451">Teacher</text></g><!--entity S--><g class="entity" data-qualified-name="S" data-source-line="4" id="ent0003"><ellipse cx="34.3457" cy="360.35" fill="#F1F1F1" rx="8" ry="8" style="stroke:#181818;stroke-width:0.5;"/><path d="M34.3457,368.35 L34.3457,395.35 M21.3457,376.35 L47.3457,376.35 M34.3457,395.35 L21.3457,410.35 M34.3457,395.35 L47.3457,410.35" fill="none" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="55.1113" x="6.79" y="424.8451">Student</text></g><!--link T to UC1--><g class="link" data-entity-1="ent0002" data-entity-2="ent0005" data-link-type="dependency" data-source-line="16" id="lnk12"><path d="M63.06,189 C91.69,189 131.6,189 170.85,189" fill="none" id="T-to-UC1" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="176.85,189,167.85,185,171.85,189,167.85,193,176.85,189" style="stroke:#181818;stroke-width:1;"/></g><!--link T to UC2--><g class="link" data-entity-1="ent0002" data-entity-2="ent0006" data-link-type="dependency" data-source-line="17" id="lnk13"><path d="M63.18,171.27 C73.93,165.06 86.55,158.51 98.68,154 C130.67,142.1 162.253,135.1445 192.003,130.1445" fill="none" id="T-to-UC2" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="197.92,129.15,188.3815,126.697,192.9892,129.9787,189.7074,134.5864,197.92,129.15" style="stroke:#181818;stroke-width:1;"/></g><!--link T to UC3--><g class="link" data-entity-1="ent0002" data-entity-2="ent0007" data-link-type="dependency" data-source-line="18" id="lnk14"><path d="M50.93,150.68 C61.41,129.66 77.24,104.91 98.68,90 C124.63,71.96 152.6713,64.2927 181.9313,60.4427" fill="none" id="T-to-UC3" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="187.88,59.66,178.4351,56.8683,182.9227,60.3123,179.4787,64.7999,187.88,59.66" style="stroke:#181818;stroke-width:1;"/></g><!--link T to UC4--><g class="link" data-entity-1="ent0002" data-entity-2="ent0008" data-link-type="dependency" data-source-line="19" id="lnk15"><path d="M50.47,227.63 C60.87,249.2 76.78,274.73 98.68,290 C126.34,309.29 157.2731,316.7405 187.7931,319.9605" fill="none" id="T-to-UC4" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="193.76,320.59,185.2294,315.6678,188.7876,320.0654,184.39,323.6236,193.76,320.59" style="stroke:#181818;stroke-width:1;"/></g><!--link T to UC5--><g class="link" data-entity-1="ent0002" data-entity-2="ent0009" data-link-type="dependency" data-source-line="20" id="lnk16"><path d="M62.88,206.51 C73.7,212.77 86.45,219.41 98.68,224 C129.03,235.4 158.4259,242.2914 187.3759,247.5314" fill="none" id="T-to-UC5" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="193.28,248.6,185.1363,243.061,188.3599,247.7095,183.7115,250.9331,193.28,248.6" style="stroke:#181818;stroke-width:1;"/></g><!--link S to UC6--><g class="link" data-entity-1="ent0003" data-entity-2="ent0010" data-link-type="dependency" data-source-line="22" id="lnk17"><path d="M62.29,407.42 C73.26,413.94 86.25,420.98 98.68,426 C124.71,436.51 148.5738,443.4878 174.7738,449.7378" fill="none" id="S-to-UC6" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="180.61,451.13,172.7838,445.1508,175.7465,449.9698,170.9275,452.9325,180.61,451.13" style="stroke:#181818;stroke-width:1;"/></g><!--link S to UC4--><g class="link" data-entity-1="ent0003" data-entity-2="ent0008" data-link-type="dependency" data-source-line="23" id="lnk18"><path d="M62.18,372.3 C73.13,365.74 86.15,358.75 98.68,354 C131.22,341.67 163.6592,334.6117 193.6992,329.6817" fill="none" id="S-to-UC4" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="199.62,328.71,190.091,326.2203,194.686,329.5197,191.3866,334.1147,199.62,328.71" style="stroke:#181818;stroke-width:1;"/></g><!--link S to UC7--><g class="link" data-entity-1="ent0003" data-entity-2="ent0011" data-link-type="dependency" data-source-line="24" id="lnk19"><path d="M62.19,390 C88.91,390 125.29,390 163.11,390" fill="none" id="S-to-UC7" style="stroke:#181818;stroke-width:1;"/><polygon fill="#181818" points="169.11,390,160.11,386,164.11,390,160.11,394,169.11,390" style="stroke:#181818;stroke-width:1;"/></g><?plantuml-src JO-n3e8m48RtUugBWz71GK7TJ8ohBWBk5pXBenP3ZnXZV7SfBOsTllxVvR_spbT1QR3LgXQiTCkbwCO0K2bDYpbJMNEBP34FKIPTnKPSb06uUJBgpZWPHKxsXYSofFZXxjdR2Zyc-07ip-pCIlT1B9gxfkAmz7PlhLPcw0XYvOKl_1U95nVDho6s8K__yh1ZL6klZetI1gUuxwJkhIx9_JdCRFnCyQn8_Bw-XQGRExRm1SXniTWDhnvf5Ic9b4PQ0sG1Dv7IIDiV?></g></svg>

---

## 📑 Example Use Case

1. Teacher creates a student profile and assigns a **Math Homework** task.  
2. Student logs in, views the task, and marks it as **Completed**.  
3. Teacher filters tasks by status to quickly see which students have finished their work.  

---

## 🚀 Tech Stack

- **Backend**: FastAPI (Python)  
- **Frontend**: React + Vite + TypeScript  
- **Database**: PostgreSQL / SQLite (configurable)  
- **Authentication**: OAuth2 with JWT tokens  
- **API Spec**: OpenAPI 3.1  

---

## 📊 ER Diagram 

```html
<?plantuml 1.2026.1beta2?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" data-diagram-type="CLASS" height="398px" preserveAspectRatio="none" style="width:221px;height:398px;background:#FFFFFF;" version="1.1" viewBox="0 0 221 398" width="221px" zoomAndPan="magnify"><defs/><g><!--class Users--><g class="entity" data-qualified-name="Users" data-source-line="1" id="ent0002"><rect fill="#F1F1F1" height="162.0781" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="207.2275" x="7" y="7"/><ellipse cx="86.7617" cy="23" fill="#ADD1B2" rx="11" ry="11" style="stroke:#181818;stroke-width:1;"/><path d="M90.8711,29 L83.1523,29 L83.1523,16.6094 L90.8711,16.6094 L90.8711,18.7656 L85.6055,18.7656 L85.6055,21.4375 L90.3711,21.4375 L90.3711,23.5938 L85.6055,23.5938 L85.6055,26.8438 L90.8711,26.8438 L90.8711,29 Z " fill="#000000"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39.2041" x="107.2617" y="27.8467">Users</text><line style="stroke:#181818;stroke-width:0.5;" x1="8" x2="213.2275" y1="39" y2="39"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="115.958" x="13" y="55.9951">id : Integer &#171;PK&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="163.5977" x="13" y="72.292">email : String &#171;unique&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="195.2275" x="13" y="88.5889">username : String &#171;unique&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="129.459" x="13" y="104.8857">first_name : String</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="127.3535" x="13" y="121.1826">last_name : String</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="180.2295" x="13" y="137.4795">hashed_password : String</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="103.1475" x="13" y="153.7764">role : UserRole</text><line style="stroke:#181818;stroke-width:0.5;" x1="8" x2="213.2275" y1="161.0781" y2="161.0781"/></g><!--class Task--><g class="entity" data-qualified-name="Task" data-source-line="11" id="ent0003"><rect fill="#F1F1F1" height="145.7813" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="188.1895" x="16.52" y="246.08"/><ellipse cx="90.0986" cy="262.08" fill="#ADD1B2" rx="11" ry="11" style="stroke:#181818;stroke-width:1;"/><path d="M94.208,268.08 L86.4892,268.08 L86.4892,255.6894 L94.208,255.6894 L94.208,257.8456 L88.9424,257.8456 L88.9424,260.5175 L93.708,260.5175 L93.708,262.6738 L88.9424,262.6738 L88.9424,265.9238 L94.208,265.9238 L94.208,268.08 Z " fill="#000000"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="32.5322" x="110.5986" y="266.9267">Task</text><line style="stroke:#181818;stroke-width:0.5;" x1="17.52" x2="203.7095" y1="278.08" y2="278.08"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="115.958" x="22.52" y="295.0751">id : Integer &#171;PK&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="176.0869" x="22.52" y="311.372">student_id : Integer &#171;FK&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="176.1895" x="22.52" y="327.6689">teacher_id : Integer &#171;FK&#187;</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="84.8682" x="22.52" y="343.9657">task : String</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="133.2393" x="22.52" y="360.2626">description : String</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="170.249" x="22.52" y="376.5595">task_status : TaskStatus</text><line style="stroke:#181818;stroke-width:0.5;" x1="17.52" x2="203.7095" y1="383.8613" y2="383.8613"/></g><!--link Users to Task--><g class="link" data-entity-1="ent0002" data-entity-2="ent0003" data-link-type="crowfoot" data-source-line="20" id="lnk4"><path codeLine="20" d="M52.9017,177.13 C47.8617,192.26 48.52,200.61 52.61,216.08 C55.24,226.02 51.4771,219.6891 55.9671,229.3091" fill="none" id="Users-Task" style="stroke:#181818;stroke-width:1;"/><line style="stroke:#181818;stroke-width:1;" x1="50.3709" x2="57.9608" y1="172.0708" y2="174.5991"/><line style="stroke:#181818;stroke-width:1;" x1="49.4227" x2="57.0127" y1="174.9171" y2="177.4454"/><line style="stroke:#181818;stroke-width:1;" x1="52.9017" x2="55.43" y1="177.13" y2="169.54"/><line style="stroke:#181818;stroke-width:1;" x1="60.1965" x2="69.017" y1="238.3707" y2="243.0824"/><line style="stroke:#181818;stroke-width:1;" x1="60.1965" x2="58.143" y1="238.3707" y2="248.1576"/><line style="stroke:#181818;stroke-width:1;" x1="60.1965" x2="63.58" y1="238.3707" y2="245.62"/><ellipse cx="57.6589" cy="232.9338" fill="none" rx="4" ry="4" style="stroke:#181818;stroke-width:1;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68.0596" x="53.61" y="212.1469">student_id</text></g><!--link Users to Task--><g class="link" data-entity-1="ent0002" data-entity-2="ent0003" data-link-type="crowfoot" data-source-line="21" id="lnk5"><path codeLine="21" d="M126.4948,177.5334 C127.9748,192.9434 127.79,201.01 126.61,216.08 C125.86,225.72 127.1148,217.9914 125.7748,227.9314" fill="none" id="Users-Task-1" style="stroke:#181818;stroke-width:1;"/><line style="stroke:#181818;stroke-width:1;" x1="122.1307" x2="130.0941" y1="173.9341" y2="173.1693"/><line style="stroke:#181818;stroke-width:1;" x1="122.4175" x2="130.3809" y1="176.9203" y2="176.1555"/><line style="stroke:#181818;stroke-width:1;" x1="126.4948" x2="125.73" y1="177.5334" y2="169.57"/><line style="stroke:#181818;stroke-width:1;" x1="124.4388" x2="129.3162" y1="237.8417" y2="246.5716"/><line style="stroke:#181818;stroke-width:1;" x1="124.4388" x2="117.4238" y1="237.8417" y2="244.9684"/><line style="stroke:#181818;stroke-width:1;" x1="124.4388" x2="123.37" y1="237.8417" y2="245.77"/><ellipse cx="125.2404" cy="231.8955" fill="none" rx="4" ry="4" style="stroke:#181818;stroke-width:1;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68.1548" x="127.61" y="212.1469">teacher_id</text></g><?plantuml-src XP3H2e8m58RlznJ3Urz0nCiWkeciQndkf2FTREUC2EtTsxGGGsbNs__zRDyPQ5Bqv1S4Yxndt2ybUSBtcg02ozFqUCYoCOTMgCQZdApIbITEgxk33tN-1YrQs2nSbKKg5fKnRyHgN0kiGHQTG7mOAvVGcYRKW_N9RzcBCPW6EGky_Pa3oKdVBdxuxii9H5c3tURXYOME12ojwaWPlGIXMY09SkX1SCl7Gn2UldmOujZqatR2ezajMY_CSj4R?></g></svg>
```



---

## 🧪 Testing

- **Backend**: Pytest (unit + integration tests).  


---

## ⚙️ Getting Started

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```
- Swagger UI → `http://localhost:8080/docs`  
- ReDoc → `http://localhost:8080/redoc`  

### Frontend
```bash
cd frontend
npm install
npm run dev
```
- Local Dev → `http://localhost:5173`  

---

## 📌 Notes

- Backend and frontend have **separate README files** for deeper documentation.  
- This README serves as the **unified overview** of the project.  
- ER diagram placeholder included for future visualization.  

---
