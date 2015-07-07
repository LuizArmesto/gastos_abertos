# -*- coding: utf-8 -*-

from sqlalchemy import and_, extract, func
from datetime import datetime

from flask import Blueprint
from flask.ext import restful
from flask.ext.restful import fields
# from flask.ext.restful.utils import cors
from flask.ext.restful.reqparse import RequestParser

from .models import Execucao
from gastosabertos.extensions import db

# Blueprint for Execucao
execucao = Blueprint('execucao', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/execucao/static')


# Create the restful API
execucao_api = restful.Api(execucao, prefix="/api/v1/execucao")


class ExecucaoInfoApi(restful.Resource):

    def get(self):
        dbyears = db.session.query(
            Execucao.data['cd_anoexecucao']).distinct().all()
        years = sorted([str(i[0]) for i in dbyears])

        return {
            "data": {
                "years": years,
            }
        }


execucao_api.add_resource(ExecucaoInfoApi, '/info')