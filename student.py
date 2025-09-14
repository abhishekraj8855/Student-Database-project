#  Required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #new random choice ke liye

# Class for Student Data Analysis
class StudentData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)

            # Standardize course names
            self.df['course'] = self.df['course'].str.strip()  #extra space remove
            self.df['course'] = self.df['course'].str.title()  #first letter capitalize
            self.df['course'] = self.df['course'].replace({
                'Data Science': 'Data Science',
                'Web Development': 'Web Development'
            
            })

            # 

            # Add year column (1st,2nd,3rd year randomly)
            self.df['year'] = np.random.choice(['1st year', '2nd year', '3rd year'], size=len(self.df))
            
            print(" Data loaded successfully!\n")
            print(self.df.head())
        except Exception as e:
            print(f" Error: {e}")

    def average_marks(self):
        if self.df is not None:
            avg = self.df['marks'].mean()
            print(f"\n📊 Average Marks: {avg:.2f}")
        else:
            print("Load data first.")

    def top_students(self, n=3):
        if self.df is not None:
            top = self.df.sort_values(by='marks', ascending=False).head(n)
            print(f"\n🏆 Top {n} Students:")
            print(top[['name', 'marks']])
        else:
            print(" Load data first.")

    def course_wise_count(self):
        if self.df is not None:
            count = self.df['course'].value_counts()
            print("\nCourse-wise Student Count:")
            print(count)
        else:
            print("Load data first.")

    def total_students(self):
        if self.df is not None:
            total = len(self.df)
            print(f"\n👨‍🎓 Total Students: {total}")
        else:
            print("su Load data first.")

    def total_subjects(self):
        if self.df is not None:
            unique_subjects = self.df['course'].nunique()  #unique subject count
            subject_list = self.df['course'].unique()  #subject ka nam
            print(f"\n Total Subjects {unique_subjects}")
            print("Subjects:", ",".join(subject_list))
        else:
            print("Load data first")
            

   


    def plot_course_distribution(self, ax=None):
        if self.df is not None:
            course_counts = self.df['course'].value_counts()
            if ax is None:
                ax = plt.gca()
            course_counts.plot(kind='bar', color='skyblue')
            plt.title(" Students per Course")
            plt.xlabel("Course")
            plt.ylabel("Number of Students")
            plt.xticks(rotation=20)
            plt.grid(axis='y')
            plt.savefig("course_distribution.png")  # Graph ko image mein save kar diya
            print(" Graph saved as 'course_distribution.png'")
            
        else:
            print(" Load data first.")

    def plot_course_pie(self, ax=None):
         if self.df is not None:
             course_counts = self.df['course'].value_counts()
             if ax is None:
                 ax = plt.gca()
             course_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='tab20')
             plt.title("Course Distribution (%)")
             plt.ylabel("")
             plt.savefig("Course_pie.png")
             print("Graph saved as 'course_pie.png'")
             plt.close()
         else:
             print("Load data first")

    def plot_year_trend(self, ax=None):
        if self.df is not None:
            self.df['year']=pd.Categorical(self.df['year'],categories=['1st year','2nd year','3rd year'],ordered=True)
            year_counts = self.df['year'].value_counts().sort_index()
            if ax is None:
                ax = plt.gca()
            year_counts.plot(kind='line',marker='o',color='green')
            plt.title("Year wise Student trend")
            plt.xlabel("Year")
            plt.ylabel("Number of Students")
            plt.grid(False)
            plt.savefig("year_trnd.png")
            print("Graph saved as 'year_trend.png'")
            plt.close()
        else:
            print("Load data first")

    def plot_marks_histogram(self, ax=None):
        if self.df is not None:
            if ax is None:
                ax = plt.gca()
            self.df['marks'].plot(kind='hist', bins=50, color='orange', edgecolor='black')
            plt.title("Marks Distribution")
            plt.xlabel("Marks")
            plt.ylabel("Frequency")
            plt.grid(axis='y')
            plt.savefig("marks_histogram.png")
            print(" Graph saved as 'marks_histogram.png'")
            plt.close()
        else:
            print("Load data first.")

    # def plot_all_charts(self):
    #     if self.df is not None:
    #         fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    #         self.plot_course_distribution(axes[0, 0])
    #         self.plot_course_pie(axes[0, 1])
    #         self.plot_year_trend(axes[1, 0])
    #         self.plot_marks_histogram(axes[1, 1])

    #         plt.suptitle("Student Data Analysis - All Charts", fontsize=16)
    #         plt.tight_layout(rect=[0, 0, 1, 0.96])
           
    #         plt.savefig("all_charts.png")
    #         print(" Graph saved as 'all_charts.png'")
    #         plt.close()
    
    #     else:
    #         print("Load data first")
       
        

# 🏁 Run the analysis
student_data = StudentData("studentsheet.csv")
student_data.load_data()
student_data.average_marks()
student_data.top_students()
student_data.course_wise_count()
student_data.plot_course_distribution()
student_data.total_students()
student_data.total_subjects()
student_data.plot_course_pie()
student_data.plot_year_trend()
student_data.plot_marks_histogram()
# student_data.plot_all_charts()