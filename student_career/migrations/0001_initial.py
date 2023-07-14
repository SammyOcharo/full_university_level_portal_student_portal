# Generated by Django 4.2.3 on 2023-07-14 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
                ('unit_code', models.CharField(max_length=100)),
                ('unit_description', models.CharField(max_length=100)),
                ('unit_instructor', models.CharField(max_length=100)),
                ('unit_schedule', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'course_unit',
            },
        ),
        migrations.CreateModel(
            name='FacultySchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_code', models.CharField(max_length=40)),
                ('school_name', models.CharField(max_length=40)),
                ('school_dean', models.CharField(max_length=50)),
                ('school_description', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='SchoolFacultyDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
                ('department_code', models.CharField(max_length=40)),
                ('department_chairman', models.CharField(max_length=50)),
                ('department_description', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_career.facultyschool')),
            ],
            options={
                'db_table': 'school_department',
            },
        ),
        migrations.CreateModel(
            name='StudentCourseInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_ID', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=255)),
                ('course_duration', models.CharField(max_length=50)),
                ('course_instructor', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student_course',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('national_id_number', models.CharField(max_length=9)),
                ('school_id_number', models.CharField(max_length=10)),
                ('status', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_career.studentcourseinformation')),
                ('department', models.ManyToManyField(to='student_career.schoolfacultydepartment')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_career.facultyschool')),
                ('units', models.ManyToManyField(related_name='students', to='student_career.courseunits')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradings', to='student_career.student')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradings', to='student_career.courseunits')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('withdrawal_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('enrolled', 'Enrolled'), ('dropped', 'Dropped'), ('completed', 'Completed')], max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='student_career.student')),
                ('units', models.ManyToManyField(related_name='enrollments', to='student_career.courseunits')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weightage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='student_career.courseunits')),
            ],
        ),
    ]