from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


#Secondary use/Relationships
class FacultySchool(models.Model):
    school_code = models.CharField(max_length=40)
    school_name = models.CharField(max_length=40)
    school_dean = models.CharField(max_length=50)
    school_description = models.CharField(max_length=255)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'school'

    def __str__(self) -> str:
        return f'{self.school_code}-{self.school_name}'


class SchoolFacultyDepartment(models.Model):
    school = models.ForeignKey(FacultySchool, on_delete=models.DO_NOTHING)
    department_name = models.CharField(max_length=30)
    department_code = models.CharField(max_length=40)
    department_chairman = models.CharField(max_length=50)
    department_description = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'school_department'

    def __str__(self):
        return self.department_name

#Course Information model
class StudentCourseInformation(models.Model):
    course_name = models.CharField(max_length=50)
    course_ID = models.CharField(max_length=50)
    course_description = models.CharField(max_length=255)
    course_duration = models.CharField(max_length=50)
    course_instructor = models.CharField(max_length= 100)

    class Meta:
        db_table = 'student_course'

    def __str__(self):
        return self.course_name
    
# Unit Information
class CourseUnits(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_code = models.CharField(max_length=100)
    unit_description = models.CharField(max_length=100)
    unit_instructor = models.CharField(max_length=100)
    unit_schedule = models.CharField(max_length=100)

    class Meta:
        db_table = 'course_unit'

    def __str__(self):
        return self.unit_name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    student_name = models.CharField(max_length=50)
    national_id_number = models.CharField(max_length=9)
    school = models.ForeignKey(FacultySchool, on_delete=models.DO_NOTHING)
    department = models.ManyToManyField(SchoolFacultyDepartment)
    school_id_number = models.CharField(max_length=10)
    course = models.ForeignKey(StudentCourseInformation, on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)
    units = models.ManyToManyField(CourseUnits, related_name='students')

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        db_table = 'student'

    

# Enrollment Management

class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('enrolled', 'Enrolled'),
        ('dropped', 'Dropped'),
        ('completed', 'Completed'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    units = models.ManyToManyField('CourseUnits', related_name='enrollments')
    enrollment_date = models.DateField()
    withdrawal_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


# Grading and Assessment

class Grading(models.Model):
    unit = models.ForeignKey('CourseUnits', on_delete=models.CASCADE, related_name='gradings')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='gradings')
    grade = models.DecimalField(max_digits=5, decimal_places=2)

class Assessment(models.Model):
    unit = models.ForeignKey('CourseUnits', on_delete=models.CASCADE, related_name='assessments')
    name = models.CharField(max_length=100)
    weightage = models.DecimalField(max_digits=5, decimal_places=2)


# Attendance Tracking
# Communication and Notifications
# Resources and Materials