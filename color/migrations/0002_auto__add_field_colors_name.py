# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Colors.name'
        db.add_column(u'color_colors', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Colors.name'
        db.delete_column(u'color_colors', 'name')


    models = {
        u'color.colors': {
            'Meta': {'object_name': 'Colors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['color']