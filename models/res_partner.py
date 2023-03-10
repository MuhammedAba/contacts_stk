# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

    partner_identity = fields.Char(String="Identification Number")
    partner_member_types = fields.Many2one("partner.member.types", string="Member types")
    partner_blood_groups = fields.Many2one("partner.blood.groups", string="Blood Groups")
    partner_gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    partner_birth_year = fields.Date(string="Birth Year")
    partner_birth_place = fields.Char( string="Place Of Birth")
    partner_birth_certificate = fields.Char(string="Birth Certificate") 
    # partner_driving_license = fields.Many2one("partner.driving.license", string="Driving License")
    partner_driving_license = fields.Many2many("partner.driving.license", string="Driving License")
    partner_education_status = fields.Many2one("partner.education.status", string="Education Status")
    partner_profession_workplace = fields.Char(string="Profession/Workplace")
    partner_sector = fields.Char(string="Sector")
    partner_languages = fields.Char(string="Languages")
    partner_passport = fields.Selection([("yes", "Yes"), ("no", "No")], default="Yes", string="Do you have a passport?")
    partner_before_ngo = fields.Selection([("yes", "Yes"), ("no", "No")] ,default="Yes",string="Do you have an NGO that you are a member of?")
    partner_family_ngo = fields.Selection([("yes", "Yes"), ("no", "No")] , default="Yes",string="Is there anyone in the family with an NGO?" )
    partner_conviction = fields.Char(string="If there is a sentence of conviction, the article and the reason.")
