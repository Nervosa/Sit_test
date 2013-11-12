# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.description'
        db.alter_column(u'products_product', 'description', self.gf('django.db.models.fields.TextField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'Product.description'
        db.alter_column(u'products_product', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'height': ('django.db.models.fields.FloatField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.FloatField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['products']