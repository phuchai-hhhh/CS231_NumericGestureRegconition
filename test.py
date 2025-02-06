USE Marriage_Hall
GO

-- NhanVien
CREATE TABLE NhanVien
(
	id int identity(1,1) primary key,
	MaNhanVien VARCHAR(100) UNIQUE,
	HoTen NVARCHAR(100) NOT NULL,
	NgaySinh DATE NOT NULL,
	GioiTinh NVARCHAR(50) CHECK (GioiTinh IN (N'Nam', N'Nữ')),
	DiaChi NVARCHAR(100),
	DienThoai NVARCHAR(100),
	Email NVARCHAR(100),
	TenDangNhap NVARCHAR(100),
	NgayVaoLam DATE NOT NULL,
	CaLam NVARCHAR(20),
	ChucVu NVARCHAR(50) CHECK (ChucVu IN (N'Phục Vụ', N'Giám Sát', N'Quản Lý')),
	Luong MONEY
)
GO

-- TaiKhoan
Create table TaiKhoan
(
	id int identity(1,1) primary key,
	TenDangNhap nvarchar(100) not null,
	MatKhau nvarchar(1000 ) not null,
	MaNhanVien VARCHAR(100) NOT NULL, 
    FOREIGN KEY (MaNhanVien) REFERENCES NhanVien(MaNhanVien)
)
GO

INSERT INTO TaiKhoan VALUES (N'PhucHai', N'1', N'NV1')
INSERT INTO TaiKhoan VALUES (N'MinhHai', N'1', N'NV2')
INSERT INTO TaiKhoan VALUES (N'TueDuc', N'1', N'NV3')
INSERT INTO TaiKhoan VALUES (N'VanGiap', N'1', N'NV4')
INSERT INTO TaiKhoan VALUES (N'DangKhoa', N'1', N'NV5')
GO

-- ThongTinSanh
Create table ThongTinSanh
(
	id int identity(1,1) primary key,
	LoaiSanh nvarchar(100) ,
	TenSanh nvarchar(100) not null default N'Chưa Đặt Tên',
	SoLuongBanToiDa int not null,
	DonGiaToiThieu money not null,
	GhiChu nvarchar(100) default N'Trống',
	TiSoPhat float default 0.01
)
GO

INSERT INTO ThongTinSanh VALUES (N'Loai A', N'Kim Cương', 500, 50000000, N'Không', 0.01)
INSERT INTO ThongTinSanh VALUES (N'Loai B', N'Bạch Kim', 450, 45000000, N'Không', 0.01)
INSERT INTO ThongTinSanh VALUES (N'Loai C', N'Vàng', 400, 40000000, N'Không', 0.01)
INSERT INTO ThongTinSanh VALUES (N'Loai D', N'Bạc', 350, 35000000, N'Không', 0.01)
INSERT INTO ThongTinSanh VALUES (N'Loai E', N'Đồng', 300, 30000000, N'Không', 0.01)
GO

-- ThucDon
Create table ThucDon
(
	id int identity,
	MaThucDon varchar(100),
	MonKhaiVi nvarchar(100) not null,
	MonChinh1 nvarchar(100)not null,
	MonChinh2 nvarchar(100) not null,
	MonChinh3 nvarchar(100) not null,
	Lau nvarchar(100) not null,
	TrangMieng nvarchar(100) not null,
	Bia nvarchar(100) not null,
	NuocNgot nvarchar(100)not null,
	GiaThucDon money not null,
	primary key(id)
)
GO

INSERT INTO ThucDon VALUES (N'TĐ 1', N'Chả Giò Rế Hà Nội', N'Gà Ấp Chảo + Bánh Bao', N'Dê Hấp Lá Tía Tô', N'Tôm Sông Rang Muối', N'Lẩu Thái Hải Sản', N'Thanh Nhiệt Sâm Sâm', N'Heniken', N'Pepsi', 2000000)
INSERT INTO ThucDon VALUES (N'TĐ 2', N'Suop Cua Gà Xé', N'Gà Bó Xôi', N'Bò Nấu Đậu + Bánh Mì', N'Vịt Quay Bắc Kinh', N'Lẩu Nắm Hải Sản', N'Chè Hạt Sen', N'Tiger Bạc', N'Trà Xanh', 1800000)
INSERT INTO ThucDon VALUES (N'TĐ 3', N'Gỏi Gó Sen Tôm Thit', N'Gà Hấp Hành + Xôi', N'Cá Điêu Hồng Chưng Tương', N'Chim Cút Roti + Bánh Mì', N'Lẩu Thái Hải Sản', N'Chè Hạt Sen', N'Heniken', N'Cocacola', 2000000)
INSERT INTO ThucDon VALUES (N'TĐ 4', N'Suop Hải Sản Nấm Tuyết', N'Gà Nấu Lagu + Bánh Mì', N'Cá Điêu Hồng Hấp HongKong', N'Gà Bó Xôi', N'Lẩu Cua Đồng', N'Rau Câu Ngũ Sắc', N'Tiger', N'Pepsi', 1800000)
INSERT INTO ThucDon VALUES (N'TĐ 5', N'Chả Giò Venus', N'Chim Cút Roti + Bánh Mì', N'Tôm Sông Rang Muối', N'Cá Điêu Hồng Chưng Tương', N'Lẩu Cá Bớp', N'Chè Khúc Bạch', N'Heniken', N'Pepsi', 2000000)
GO

-- DichVu
create table DichVu
(
	id int identity ,
	MaDichVu  varchar(100),
	Ruou nvarchar(100),
	BanhKem nvarchar(100),
	Mc nvarchar(100),
	BanNhac nvarchar(100),
	CaSi nvarchar(100),
	Dj nvarchar(100),
	GiaDichVu money,
	primary key(id)
)
GO

INSERT INTO DichVu VALUES (N'DV1', N'Rượu Vang', N'2 Tầng', N'Minh Anh', N'Band 1', N'NhưYến', N'Dan', 1000000)
INSERT INTO DichVu VALUES (N'DV2', N'Rượu Vang', N'3 Tầng', N'Ngọc Như', N'Band 2', N'NgọcBích', N'Black', 2000000)
INSERT INTO DichVu VALUES (N'DV3', N'Rượu Vang', N'4 Tầng', N'Anh Tuấn', N'Band 3', N'HoàngNgọc', N'DN', 3000000)
INSERT INTO DichVu VALUES (N'DV4', N'Rượu Vang', N'5 Tầng', N'Tuấn Khang', N'Band 4', N'NguyênKhang', N'Mie', 4000000)
GO

-- Tiec
Create table Tiec
(
	id  int identity(1,1),
	Ca nvarchar(20),
	TrangThai nvarchar(100) default N'Chưa săn sàng'
)
GO

INSERT INTO Tiec VALUES (N'Trưa', N'Chưa sẵn sàng')
INSERT INTO Tiec VALUES (N'Tối', N'Sẵn sàng')
GO

-- ThongTinKhachHang
Create table ThongTinkhachHang
(
	id int identity(1,1),
	MaKhachHang  AS RIGHT('KH' + CAST(id AS VARCHAR(7)), 7) PERSISTED,
	NgayLap date not null,
	TenKhachHang nvarchar(100) not null,
	TenChuRe nvarchar(100) not null,
	TenCoDau nvarchar(100) not null,
	DiaChi nvarchar(100) not null,
	DienThoai nvarchar(100) not null,
	Email nvarchar(100) not null,
	NgayToChuc date not null,
	TienCoc money,
	primary key(id)
)
GO

INSERT INTO ThongTinKhachHang VALUES ('2018-12-03', N'Nguyễn Thành Tài', N'Nguyễn Thành Tài', N'Hoàng Thị Bích Ngọc', N'Thị Trấn Bến Cầu, Huyện Bến Cầu, Tỉnh Tây Ninh', N'0169356263', N'nguyentai23998@gmail.com', '2018-12-12', 5000000)
INSERT INTO ThongTinKhachHang VALUES ('2018-10-04', N'Hà Như Ý', N'Hà Như Ý', N'Nguyễn Thị Tố Như', N'Phường Linh Trung, Quận Thủ Đức, Tp.Hồ Chí Minh', N'016253625', N'nhuy1998@gmail.com', '2018-12-12', 4000000)
INSERT INTO ThongTinKhachHang VALUES ('2018-10-02', N'Hà Như', N'Hà Như', N'Nguyễn Thị Tố', N'Phường Linh Trung, Quận Thủ Đức, Tp.Hồ Chí Minh', N'01623453', N'nhu1998@gmail.com', '2018-12-01', 3000000)
GO

-- ThongTinDatTiec
Create table ThongTinDatTiec
(
	id int identity(1,1) primary key,
	MaDatTiec  AS RIGHT('DT' + CAST(id AS VARCHAR(7)), 7) PERSISTED,
	IDNhanVien int FOREIGN KEY REFERENCES NhanVien(id),
	IDThongTinKhachHang int FOREIGN KEY REFERENCES ThongTinKhachHang(id),
	IdLoaiSanh int FOREIGN KEY REFERENCES ThongTinSanh(id),
	IdDichVu int FOREIGN KEY REFERENCES DichVu(id),
	IdThucDon int FOREIGN KEY REFERENCES ThucDon(id),
	SoLuongNhanVien int not null,
	SoLuongBan int,
	Ca nvarchar(100) CHECK (Ca IN (N'Trưa', N'Tối'))
)
GO

-- HoaDon
Create table HoaDon
(
	id int identity(1,1) primary key,
	MaHoaDon  AS RIGHT('HĐ' + CAST(id AS VARCHAR(7)), 7) PERSISTED,
	IdMaDatTiec int FOREIGN KEY REFERENCES ThongTinDatTiec(id),
	IDThongTinKhachHang int FOREIGN KEY REFERENCES ThongTinKhachHang(id),
	IdLoaiSanh int FOREIGN KEY REFERENCES ThongTinSanh(id),
	IdDichVu int FOREIGN KEY REFERENCES DichVu(id),
	IdThucDon int FOREIGN KEY REFERENCES ThucDon(id),
	TienPhat money,
	TongTienHoaDon money not null,
	TienCoc money not null,
	TienConLai money 
)
GO

-- LapBaoCao
Create table LapBaoCao
(
	id int identity(1,1) primary key,
	MaBaoCao AS RIGHT('BC00' + CAST(id AS VARCHAR(5)), 5) PERSISTED,
	NgayLap date not null,
	TenNguoiLap nvarchar(100),
	Thang int,
	SoLuongTiec int,
	DoanhThu MONEY
)
GO

-- BaoCaoDoanhThu
Create table BaoCaoDoanhThu
(
	id int identity(1,1) primary key,
	Thang int,
	TongDoanhThu MONEY
)
GO
