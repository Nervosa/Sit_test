# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.FloatField')(max_length=10)),
            ('weight', self.gf('django.db.models.fields.FloatField')(max_length=10)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
        ))
        db.send_create_signal(u'products', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'products_product')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'height': ('django.db.models.fields.FloatField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.FloatField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['products']