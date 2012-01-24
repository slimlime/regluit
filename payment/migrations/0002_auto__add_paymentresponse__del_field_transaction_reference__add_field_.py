# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PaymentResponse'
        db.create_table('payment_paymentresponse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('api', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('correlation_id', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payment.Transaction'])),
        ))
        db.send_create_signal('payment', ['PaymentResponse'])

        # Deleting field 'Transaction.reference'
        db.delete_column('payment_transaction', 'reference')

        # Adding field 'Transaction.execution'
        db.add_column('payment_transaction', 'execution', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Transaction.pay_key'
        db.add_column('payment_transaction', 'pay_key', self.gf('django.db.models.fields.CharField')(max_length=128, null=True), keep_default=False)

        # Adding field 'Transaction.preapproval_key'
        db.add_column('payment_transaction', 'preapproval_key', self.gf('django.db.models.fields.CharField')(max_length=128, null=True), keep_default=False)

        # Adding field 'Transaction.date_executed'
        db.add_column('payment_transaction', 'date_executed', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'PaymentResponse'
        db.delete_table('payment_paymentresponse')

        # Adding field 'Transaction.reference'
        db.add_column('payment_transaction', 'reference', self.gf('django.db.models.fields.CharField')(max_length=128, null=True), keep_default=False)

        # Deleting field 'Transaction.execution'
        db.delete_column('payment_transaction', 'execution')

        # Deleting field 'Transaction.pay_key'
        db.delete_column('payment_transaction', 'pay_key')

        # Deleting field 'Transaction.preapproval_key'
        db.delete_column('payment_transaction', 'preapproval_key')

        # Deleting field 'Transaction.date_executed'
        db.delete_column('payment_transaction', 'date_executed')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'activated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'amazon_receiver': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'managers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'campaigns'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'paypal_receiver': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'INITIALIZED'", 'max_length': '15', 'null': 'True'}),
            'target': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaigns'", 'to': "orm['core.Work']"})
        },
        'core.wishes': {
            'Meta': {'object_name': 'Wishes', 'db_table': "'core_wishlist_works'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'wishlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Wishlist']"}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Work']"})
        },
        'core.wishlist': {
            'Meta': {'object_name': 'Wishlist'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'wishlist'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'works': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wishlists'", 'symmetrical': 'False', 'through': "orm['core.Wishes']", 'to': "orm['core.Work']"})
        },
        'core.work': {
            'Meta': {'ordering': "['title']", 'object_name': 'Work'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'librarything_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'openlibrary_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'payment.paymentresponse': {
            'Meta': {'object_name': 'PaymentResponse'},
            'api': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'correlation_id': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['payment.Transaction']"})
        },
        'payment.receiver': {
            'Meta': {'object_name': 'Receiver'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '14', 'decimal_places': '2'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['payment.Transaction']"}),
            'txn_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'payment.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '14', 'decimal_places': '2'}),
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Campaign']", 'null': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '10', 'null': 'True'}),
            'date_authorized': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_executed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_expired': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_payment': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'execution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Wishlist']", 'null': 'True'}),
            'pay_key': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'preapproval_key': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'receipt': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '32'}),
            'target': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['payment']