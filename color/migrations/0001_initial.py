# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Colors'
        db.create_table(u'color_colors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'color', ['Colors'])


    def backwards(self, orm):
        # Deleting model 'Colors'
        db.delete_table(u'color_colors')


    models = {
        u'color.colors': {
            'Meta': {'object_name': 'Colors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['color']