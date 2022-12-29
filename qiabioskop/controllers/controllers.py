from odoo import http, models, fields
from odoo.http import request
from datetime import datetime
import json

class Qiabioskop(http.Controller):
    @http.route('/qiabioskop/gettiket', auth='public', method=['GET'])
    def getTiket(self, **kw):
        tiket = request.env['qiabioskop.tiket'].search([])
        isi = []
        for kk in tiket:
            isi.append({
                'kode_tiket' : kk.name,
                'harga_jual' : kk.harga_jual,
                'stok' : kk.stok,
                'kursi' : kk.kursi_id[0].name
            })
        return json.dumps(isi)

    @http.route('/qiabioskop/getfilm', auth='public', method=['GET'])
    def getFilm(self, **kw):
        film = request.env['qiabioskop.film'].search([])
        sup = []
        for ss in film:
            sup.append({
                'judul_film' : ss.name, 
                'durasi' : ss.durasi,
                'produser' : ss.produser,
                'sutradara' : ss.sutradara,
                'penulis' : ss.penulis,
                'aktor' : ss.aktor,
                'sinopsis' : ss.sinopsis,
                'genre' : ss.genre_no[0].name,
                'studio' : ss.studio_ids[0].name,
                'jadwal' : ss.jadwal_ids.name   
                }) 
        
        def date_handler(obj):
            return obj.isoformat() if hasattr(obj, 'isoformat') else obj
        return json.dumps(sup, default=date_handler)
    
    @http.route('/qiabioskop/getjadwal', auth='public', method=['GET'])
    def getJadwal(self, **kw):
        jadwal = request.env['qiabioskop.jadwal'].search([])
        jad = []
        for jj in jadwal:
            jad.append({
                'tanggal_tayang' : jj.name,
                'jam_mulai' : jj.jam_mulai,
                'jam_berakhir' : jj.jam_berakhir,
                'daftar_pelanggan' : jj.pelanggan_id[0].id,
                'daftar_film' : jj.film_id[0].name
            })
        def date_handler(obj):
            return obj.isoformat() if hasattr(obj, 'isoformat') else obj
        return json.dumps(jad, default=date_handler)
    
    @http.route('/qiabioskop/getgenre', auth='public', method=['GET'])
    def getGenre(self, **kw):
        genre = request.env['qiabioskop.genre'].search([])
        gen = []
        for gg in genre:
            gen.append({
                'nama_genre' : gg.name,
                'kode_genre' : gg.kd_genre,
                'daftar_film' : gg.film_ids[0].name,
                'jumlah_film' : gg.film_ids[0].name,
                'pilihan' : gg.film_ids[0].name
            })
        return json.dumps(gen)

    @http.route('/qiabioskop/getkursi', auth='public', method=['GET'])
    def getKursi(self, **kw):
        kursi = request.env['qiabioskop.kursi'].search([])
        kur = []
        for kk in kursi:
            kur.append({
                'nomor_kursi' : kk.name,
                'kode_kursi' : kk.kd_kursi,
                'tiket' : kk.tiket_ids[0].name,
                'daftar_studio' : kk.studio_id[0].name
            })
        return json.dumps(kur)

    @http.route('/qiabioskop/getstudio', auth='public', method=['GET'])
    def getStudio(self, **kw):
        studio = request.env['qiabioskop.studio'].search([])
        stu = []
        for ii in studio:
            stu.append({
                'nama_studio' : ii.name,
                'kode_studio' : ii.kd_studio,
                'daftar_kursi' : ii.kursi_ids[0].name,
                'jumlah_kursi' : ii.kursi_ids[0].name,
                'pilihan' : ii.pilihan,
                'daftar_film' : ii.film_studio_id[0].name
            })
        return json.dumps(stu)

    @http.route('/qiabioskop/getpenjualan', auth='public', method=['GET'])
    def getStudio(self, **kw):
        penjualan = request.env['qiabioskop.penjualan'].search([])
        pen = []
        for nn in penjualan:
            pen.append({
                'no_nota' : nn.name,
                'nama_pembeli' : nn.id,
                'ID_member' : nn.id_member,
                'tanggal_penjualan' : nn.tgl_penjualan,
                'ttl_bayar' : nn.total_bayar,
                'detail_penjualan' : nn.detailpenjualan_ids[0].name,
                'status' : nn.state,
            })
        return json.dumps(pen)

    

        