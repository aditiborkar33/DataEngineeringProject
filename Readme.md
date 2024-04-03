This Assignment contains:

REQUIREMENT:
</br></br> 1. With the help of Python find out the answers to the below questions for the attached
Healthcare_Data.zip:
</br>a. Create a plot to find out if there is any co-relation between the Blood Group Type,
Gender and the Medical Condition?
</br>b. Find out the Average Billing Amount required to treat each medical Condition?
</br></br> 2. Using the Healthcare Data as training data and the insights from the co-relation achieved above:
</br>a. Create a Web Application (Web Form) where Users can enter their Name, Gender and
Blood Group and it should show them the Medical Condition they are at most risk.
</br>b. All the Data Entered by the users (Name, Gender, Blood Group) should be stored at the
back end in a separate csv/json file.
</br></br></br>

Solution:
1.
a: 
Prerequisites:
Install below libraries using PIP

matplotlib.pyplot
pandas
seaborn

run:  python3 HealthcareDataAnalysis.py 
Output: path![Screenshot 2024-04-03 at 11.03.58 PM.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F86%2Fb0348_xx4sbcb0vcx56n4j4w0000gp%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_BkdLK6%2FScreenshot%202024-04-03%20at%2011.03.58%E2%80%AFPM.png)

b: 
run:  python3 HealthcareDataAnalysis.py 
output: 
Medical Condition </t>      AVGBill</br>
0   </t>        Arthritis </t>   25187.631255</br>
1   </t>           Asthma </t>   25416.869895</br>
2   </t>           Cancer </t>   25539.096133</br>
3   </t>        Diabetes  </t>   26060.116129</br>
4   </t>    Hypertension  </t>   25198.033973</br>
5   </t>         Obesity  </t>   25720.842683</br>

This output will get printed in <b>Terminal</b>

2.
a:
Created Website open index.html in browser, css file is linked with it named styles.css
WebApi.py file will be used to start server on http://127.0.0.1:5000 using Flask

api exposed is /submit which will accept POST request 
User will fillup all data in web form and submit. CSV file with name patient_data.csv will get created and User Data will be inserted.

![Screenshot 2024-04-03 at 11.14.35 PM.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F86%2Fb0348_xx4sbcb0vcx56n4j4w0000gp%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_25CFRJ%2FScreenshot%202024-04-03%20at%2011.14.35%E2%80%AFPM.png)

b: 