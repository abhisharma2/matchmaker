from django.db import models

Class Program(models.Model):
    nbcu_program: models.BooleanField
    program_net_name: models.CharField(max_length=255)
    network: models.CharField(max_length=255)
    program_name: models.CharField(max_length=255)
    network_id: models.IntegerField

Class CorrelationScore(models.Model):
    program_id: models.IntegerField
    match_program_id: models.ForeignKey(Program)
    total_p2_match_score: models.DecimalField(max_digits=16, decimal_places=8)
    total_match_score: models.DecimalField(max_digits=16, decimal_places=8)
    weighted_score: models.DecimalField(max_digits=16, decimal_places=8)
    vb_score: models.DecimalField(max_digits=16, decimal_places=8)
    demo_score: models.DecimalField(max_digits=16, decimal_places=8)
    format_score: models.DecimalField(max_digits=16, decimal_places=8)
    topic_score: models.DecimalField(max_digits=16, decimal_places=8)
    political_score: models.DecimalField(max_digits=16, decimal_places=8)
    talent_score: models.DecimalField(max_digits=16, decimal_places=8)
    p2_size_score: models.DecimalField(max_digits=16, decimal_places=8)
