<<<<<<< HEAD
from django.db import models
=======
﻿from django.db import models
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
from django.utils.translation import ugettext_lazy as _

class Group(models.Model):
    class Meta(object):
        verbose_name = _(u"Group")
        verbose_name_plural = _(u"Groups")

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Title"))

    leader = models.OneToOneField('Student',
        verbose_name=_(u"Leader"),
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Extra Notes"))
	
    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                self.leader.last_name)
        else:
<<<<<<< HEAD
            return u"%s" % (self.title,)	
=======
            return u"%s" % (self.title,)	
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
