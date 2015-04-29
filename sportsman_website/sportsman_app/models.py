from django.db import models

# Query text field
class Query(models.Model):
	query_text = models.CharField(max_length=200)
	#pub_date = models.DateTimeField('date published')

	#def __str__(self):
		#return self.query_text

#Sports type selection
class SportsType(models.Model):
	query = models.ForeignKey(Query)
	ROCKCLIMBING = 'RC'
	TENNIS = 'TNS'
	SWIMMING = 'SWM'
	SKII = 'SKI'
	BASKETBALL = 'BSKB'
	SOCCER = 'SCC'
	GYM = 'GYM'
	BASEBALL = 'BSB'
	BADMINTON = 'BDMT'
	ICEHOCKEY = 'ICHC'
	GOLF = 'GLF'
	FOOTBALL = 'FTB'
	FISHING = 'FSH'
	TABLETENNIS = 'TBTN'
	SPORTSTYPE_CHOICES = (
		(ROCKCLIMBING, 'Rock Climbing'),
		(TENNIS, 'Tennis'),
		(SWIMMING, 'Swimming'),
		(SKII, 'Skii'),
		(BASKETBALL, 'Basketball'),
		(SOCCER, 'Soccer'),
		(GYM, 'Gym'),
		(BASEBALL, 'Baseball'),
		(BADMINTON, 'Badminton'),
		(ICEHOCKEY, 'Ice Hockey'),
		(GOLF, 'Golf'),
		(FOOTBALL, 'Football'),
		(FISHING, 'Fishing'),
		(TABLETENNIS, 'Table Tennis'),
	)

	sportstype_text = models.CharField(max_length=200, choices=SPORTSTYPE_CHOICES, default=GYM)

	votes = models.IntegerField(default=0)
	#def __str__(self):
		#return self.sportstype





















