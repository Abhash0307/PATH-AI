# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# from fpdf import FPDF

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# class MockInterviewer:
#     def __init__(self, resume_bytes):
#         # Parse resume bytes (placeholder for now)
#         self.resume_text = "Parsed resume text here…"  

#     def generate_questions(self):
#         prompt = f"""
#         Based on this resume: {self.resume_text},
#         generate 5 technical questions, 3 behavioral questions, and 2 coding questions
#         for a software developer role. Return as a numbered list.
#         """
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         response = model.generate_content(prompt)
#         return response.text.split("\n")

#     def analyze_answer(self, question, answer):
#         prompt = f"""
#         Evaluate this answer to the question: "{question}".
#         Answer: "{answer}".
#         Provide constructive feedback.
#         """
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         response = model.generate_content(prompt)
#         return response.text

#     def evaluate_code(self, question, code):
#         """
#         Dummy test case simulation — in production, use proper sandbox + test cases
#         """
#         # Fake: assume all code passes
#         return True  

#     def generate_feedback_pdf(self, feedback_data):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)
#         pdf.cell(200, 10, txt="Mock Interview Feedback Report", ln=True, align="C")
#         for idx, (q, a, f) in enumerate(feedback_data):
#             pdf.multi_cell(0, 10, txt=f"Q{idx+1}: {q}\nYour Answer: {a}\nFeedback: {f}\n\n")
#         return pdf.output(dest="S").encode("latin-1")

# utils/mock_interviewer.py
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# import speech_recognition as sr
# import cv2
# import threading
# import tempfile
# import subprocess

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# class MockInterviewer:
#     def __init__(self):
#         self.questions = []
#         self.feedback = []
#         self.coding_test_cases = []
#         self.recognizer = sr.Recognizer()
#         self.cap = None
#         self.camera_running = False

#     def generate_questions(self, resume_text):
#         prompt = f"""Act as an AI interviewer. Candidate's resume:\n{resume_text}\n
#         Generate 10 questions: 5 technical, 3 behavioral, and 2 coding.
#         Format coding questions as: CODING:<question>|<test_case_1>|<test_case_2> etc."""
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         response = model.generate_content(prompt)
#         for line in response.text.strip().split('\n'):
#             if line.startswith("CODING:"):
#                 q_parts = line[7:].split("|")
#                 self.questions.append(q_parts[0].strip())
#                 self.coding_test_cases.append([tc.strip() for tc in q_parts[1:]])
#             else:
#                 self.questions.append(line.strip())

#     def listen_to_answer(self, timeout=10):
#         with sr.Microphone() as source:
#             audio = self.recognizer.listen(source, timeout=timeout)
#             try:
#                 text = self.recognizer.recognize_google(audio)
#                 return text
#             except:
#                 return "Could not understand audio."

#     def analyze_answer(self, question, answer):
#         prompt = f"""You are an AI interviewer. Here is the question:\n{question}\n
#         Here is the candidate's answer:\n{answer}\n
#         Give constructive feedback."""
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         response = model.generate_content(prompt)
#         feedback = response.text.strip()
#         self.feedback.append((question, answer, feedback))
#         return feedback

#     def check_code(self, code, test_cases):
#         results = []
#         for idx, case in enumerate(test_cases, 1):
#             try:
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as tmpf:
#                     tmpf.write(code + f"\nprint({case})")
#                     tmpf_path = tmpf.name
#                 result = subprocess.run(["python", tmpf_path], capture_output=True, text=True, timeout=5)
#                 output = result.stdout.strip()
#                 results.append(f"✅ Test Case {idx}: Passed (Output: {output})")
#             except Exception as e:
#                 results.append(f"❌ Test Case {idx}: Failed ({str(e)})")
#         return "\n".join(results)

#     def start_camera(self):
#         if not self.camera_running:
#             self.cap = cv2.VideoCapture(0)
#             self.camera_running = True
#             threading.Thread(target=self._camera_loop, daemon=True).start()

#     def _camera_loop(self):
#         while self.camera_running:
#             ret, frame = self.cap.read()
#             if ret:
#                 cv2.imshow("Proctoring Camera", frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         self.cap.release()
#         cv2.destroyAllWindows()

#     def stop_camera(self):
#         self.camera_running = False

#     def generate_pdf_feedback(self, path):
#         from fpdf import FPDF
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)
#         pdf.cell(200, 10, txt="Mock Interview Feedback", ln=True, align='C')
#         for idx, (q, a, fb) in enumerate(self.feedback, start=1):
#             pdf.multi_cell(0, 10, txt=f"{idx}. Q: {q}")
#             pdf.multi_cell(0, 10, txt=f"Answer: {a}")
#             pdf.multi_cell(0, 10, txt=f"Feedback: {fb}\n")
#         pdf.output(path)




# backend.py


# backend.py
# backend.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
import speech_recognition as sr
import cv2
import threading
import tempfile
import subprocess

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not set in .env file")

genai.configure(api_key=api_key)

class MockInterviewer:
    def __init__(self):
        self.questions = []
        self.feedback = []
        self.coding_test_cases = []
        self.recognizer = sr.Recognizer()
        self.cap = None
        self.camera_running = False

    def generate_questions(self, resume_or_role_text):
        """
        Use Gemini to generate 10 questions:
        5 technical, 3 behavioral, 2 coding.
        """
        self.questions.clear()
        self.feedback.clear()
        self.coding_test_cases.clear()

        prompt = f"""
Act as a professional AI interviewer. 
Below is the candidate's resume text or preferred job role:\n\n
\"\"\"\n{resume_or_role_text}\n\"\"\"\n\n
Generate exactly 10 interview questions:
- 5 technical
- 3 behavioral
- 2 coding (include test cases in format: CODING:<question>|<test_case_1>|<test_case_2>)

Output format:
One question per line.
For coding questions, follow this format strictly.
"""

        model = genai.GenerativeModel("gemini-2.0-flash")
        try:
            response = model.generate_content(prompt, stream=False)
        except Exception as e:
            raise RuntimeError(f"Failed to generate questions: {e}")
        
        if not response.text.strip():
            raise RuntimeError("No response received from Gemini.")

        for line in response.text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            if line.startswith("CODING:"):
                parts = line[7:].split("|")
                question = parts[0].strip()
                test_cases = [tc.strip() for tc in parts[1:]]
                self.questions.append(question)
                self.coding_test_cases.append(test_cases)
            else:
                self.questions.append(line)

        # Pad coding_test_cases to match question count
        while len(self.coding_test_cases) < len(self.questions):
            self.coding_test_cases.append([])

    def listen_to_answer(self, timeout=10):
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                text = self.recognizer.recognize_google(audio)
                return text
            except Exception:
                return "Could not understand audio."

    def analyze_answer(self, question, answer):
        prompt = f"""
You are an AI interviewer. 
Here is the question:\n{question}\n
Here is the candidate's answer:\n{answer}\n
Give specific, constructive feedback in 2-3 sentences.
"""
        model = genai.GenerativeModel("gemini-2.0-flash")
        try:
            response = model.generate_content(prompt, stream=False)
        except Exception as e:
            return f"Error analyzing answer: {e}"
        
        feedback = response.text.strip()
        self.feedback.append((question, answer, feedback))
        return feedback

    def check_code(self, code, test_cases):
        results = []
        for idx, case in enumerate(test_cases, 1):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as tmpf:
                    tmpf.write(code + f"\nprint({case})")
                    tmpf_path = tmpf.name
                result = subprocess.run(["python", tmpf_path], capture_output=True, text=True, timeout=5)
                output = result.stdout.strip()
                results.append(f"✅ Test Case {idx}: Passed (Output: {output})")
            except Exception as e:
                results.append(f"❌ Test Case {idx}: Failed ({str(e)})")
        return "\n".join(results)

    def start_camera(self):
        if not self.camera_running:
            self.cap = cv2.VideoCapture(0)
            self.camera_running = True
            threading.Thread(target=self._camera_loop, daemon=True).start()

    def _camera_loop(self):
        while self.camera_running:
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow("Proctoring Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def stop_camera(self):
        self.camera_running = False

    def generate_pdf_feedback(self, path):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Mock Interview Feedback", ln=True, align='C')
        for idx, (q, a, fb) in enumerate(self.feedback, start=1):
            pdf.multi_cell(0, 10, txt=f"{idx}. Q: {q}")
            pdf.multi_cell(0, 10, txt=f"Answer: {a}")
            pdf.multi_cell(0, 10, txt=f"Feedback: {fb}\n")
        pdf.output(path)
