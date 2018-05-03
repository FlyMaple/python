# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                                                                   #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random

score = round(random.random() * 150)

if score < 60:
    print('score: %d' % score, '< 60')
elif score >= 60 and score <=79:
    print('score: %d' % score, '>= 60 and <= 79')
elif score >= 80 and score < 100:
    print('score: %d' % score, '>= 80 and < 100')
elif score == 100:
    print('score: %d' % score, '== 100')
else:
    print('????')