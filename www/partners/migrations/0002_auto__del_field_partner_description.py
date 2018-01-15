# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Partner.description'
        db.delete_column(u'partners_partner', 'description')


    def backwards(self, orm):
        # Adding field 'Partner.description'
        db.add_column(u'partners_partner', 'description',
                      self.gf('ckeditor.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


    models = {
        u'partners.partner': {
            'Meta': {'ordering': "['sort', '-id']", 'object_name': 'Partner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['partners']