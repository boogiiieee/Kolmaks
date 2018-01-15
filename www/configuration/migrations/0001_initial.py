# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConfigModel'
        db.create_table(u'configuration_configmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('office', self.gf('django.db.models.fields.CharField')(default=u'\u041c\u0435\u0441\u0442\u043e\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0444\u0438\u0441\u0430', max_length=100)),
            ('is_active_map_1', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('address1', self.gf('map2gis.django_2gis_widget.LocationField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'configuration', ['ConfigModel'])


    def backwards(self, orm):
        # Deleting model 'ConfigModel'
        db.delete_table(u'configuration_configmodel')


    models = {
        u'configuration.configmodel': {
            'Meta': {'object_name': 'ConfigModel'},
            'address1': ('map2gis.django_2gis_widget.LocationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active_map_1': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "u'\\u041c\\u0435\\u0441\\u0442\\u043e\\u0440\\u0430\\u0441\\u043f\\u043e\\u043b\\u043e\\u0436\\u0435\\u043d\\u0438\\u0435 \\u043e\\u0444\\u0438\\u0441\\u0430'", 'max_length': '100'})
        }
    }

    complete_apps = ['configuration']