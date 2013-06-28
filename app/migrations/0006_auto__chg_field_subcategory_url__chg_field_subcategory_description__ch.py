# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SubCategory.url'
        db.alter_column(u'app_subcategory', 'url', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

        # Changing field 'SubCategory.description'
        db.alter_column(u'app_subcategory', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Category.url'
        db.alter_column(u'app_category', 'url', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

        # Changing field 'Category.description'
        db.alter_column(u'app_category', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'SubCategory.url'
        db.alter_column(u'app_subcategory', 'url', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50))

        # Changing field 'SubCategory.description'
        db.alter_column(u'app_subcategory', 'description', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'Category.url'
        db.alter_column(u'app_category', 'url', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50))

        # Changing field 'Category.description'
        db.alter_column(u'app_category', 'description', self.gf('django.db.models.fields.TextField')(default=None))

    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'app.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SubCategory']"})
        },
        u'app.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['app']