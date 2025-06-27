from django.urls import path
from .views import GradeView,SectionView , generateAttendanceCsv ,uploadAttendanceExcel

urlpatterns = [
    path('grade/', GradeView.as_view(), name='grade'),
    path('section/', SectionView.as_view(), name='section'),
    path('get-attendance-csv/', generateAttendanceCsv, name='generate_csv_data'),
    path('upload-attendance-csv/', uploadAttendanceExcel, name='upload_csv_data'),

]
