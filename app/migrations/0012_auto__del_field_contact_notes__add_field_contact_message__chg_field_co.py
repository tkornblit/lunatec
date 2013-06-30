# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.notes'
        db.delete_column(u'app_contact', 'notes')

        # Adding field 'Contact.message'
        db.add_column(u'app_contact', 'message',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


        # Changing field 'Contact.phone'
        db.alter_column(u'app_contact', 'phone', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))
        # Deleting field 'Category.image'
        db.delete_column(u'app_category', 'image')


    def backwards(self, orm):
        # Adding field 'Contact.notes'
        db.add_column(u'app_contact', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Deleting field 'Contact.message'
        db.delete_column(u'app_contact', 'message')


        # Changing field 'Contact.phone'
        db.alter_column(u'app_contact', 'phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=75))
        # Adding field 'Category.image'
        db.add_column(u'app_category', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)


    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Product']", 'null': 'True', 'blank': 'True'})
        },
        u'app.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['app.SubCategory']"})
        },
        u'app.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': u"orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app']