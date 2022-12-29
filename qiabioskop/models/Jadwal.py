from odoo import api, fields, models


class Jadwal(models.Model):
    _name = 'qiabioskop.jadwal'
    _description = 'Jadwal'
       
    name = fields.Selection([
        ('14/09/2022', '14/09/2022'), 
        ('15/09/2022', '15/09/2022'), 
        ('16/09/2022', '17/09/2022'),
        ], string='Tanggal Tayang')

    jam_mulai = fields.Selection([
        ('10:00:00', '10:00:00'), 
        ('13:00:00', '13:00:00'), 
        ('15:00:00', '15:00:00'),
        ('18:15:00', '18:15:00'),
        ('20:15:00', '20:15:00'),
        ], string='Jam Mulai')

    jam_berakhir = fields.Char(onchange='_compute_jam_mulai', string='Jam Berakhir')

    @api.onchange('jam_mulai')
    def _onchange_jam_berakhir(self):
        if (self.jam_mulai == '10:00:00'):
            self.jam_berakhir = '12:40:00'
        elif (self.jam_mulai == '13:00:00'):
            self.jam_berakhir = '13:40:00'
        elif (self.jam_mulai == '15:00:00'):
            self.jam_berakhir = '17:40:00'
        elif (self.jam_mulai == '18:15:00'):
            self.jam_berakhir = '20:40:00'
        elif (self.jam_mulai == '20:15:00'):
            self.jam_berakhir = '22:45:00'
        
    pelanggan_id = fields.Many2one(comodel_name='res.partner', 
                                   string='Daftar Pelanggan',
                                   ondelete='cascade')
    film_id = fields.Many2one(comodel_name='qiabioskop.film', string='Daftar Film')
    
    
    
    
    
    
    