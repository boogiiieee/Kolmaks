# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ConfigModel.magazine'
        db.delete_column(u'configuration_configmodel', 'magazine')

        # Deleting field 'ConfigModel.office'
        db.delete_column(u'configuration_configmodel', 'office')

        # Adding field 'ConfigModel.title'
        db.add_column(u'configuration_configmodel', 'title',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0430\u0439\u0442\u0430', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ConfigModel.magazine'
        db.add_column(u'configuration_configmodel', 'magazine',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041c\u0435\u0441\u0442\u043e\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0441\u043a\u043b\u0430\u0434\u0430', max_length=100),
                      keep_default=False)

        # Adding field 'ConfigModel.office'
        db.add_column(u'configuration_configmodel', 'office',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041c\u0435\u0441\u0442\u043e\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0444\u0438\u0441\u0430', max_length=100),
                      keep_default=False)

        # Deleting field 'ConfigModel.title'
        db.delete_column(u'configuration_configmodel', 'title')


    models = {
        u'configuration.configmodel': {
            'Meta': {'object_name': 'ConfigModel'},
            'address1': ('map2gis.django_2gis_widget.LocationField', [], {'null': 'True', 'blank': 'True'}),
            'address2': ('map2gis.django_2gis_widget.LocationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active_map_1': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_map_2': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435 \\u0441\\u0430\\u0439\\u0442\\u0430'", 'max_length': '100'})
        }
    }

    complete_apps = ['configuration']