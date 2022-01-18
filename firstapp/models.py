from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # 테이블명을 curriculum 으로 지정
        db_table = 'curriculum'
        # 현재 위치(App)가 아닌 외부에 정의된 경우
        app_label = 'firstapp'
        # 데이터 조회 기본 정렬 상태
        ordering = ['-id', 'name']
        # migration 대상 여부
        managed = False
        # Create your models here.

