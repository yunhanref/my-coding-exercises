use eframe::egui;

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default().with_inner_size([300.0, 420.0]),
        ..Default::default()
    };

    eframe::run_native(
        "Rust Hesap Makinesi",
        options,
        Box::new(|_cc| Ok(Box::new(HesapMakinesi::default()))),
    )
}

// Matematiksel operatörleri tanımlıyoruz
#[derive(Clone, Copy, PartialEq)]
enum Operator {
    Topla,
    Cikar,
    Carp,
    Bol,
    Yok,
}

// Uygulamanın hafızası (State)
struct HesapMakinesi {
    ekran: String,
    onceki_sayi: f64,
    aktif_operator: Operator,
    yeni_sayi_mi: bool,
}

impl Default for HesapMakinesi {
    fn default() -> Self {
        Self {
            ekran: "0".to_string(),
            onceki_sayi: 0.0,
            aktif_operator: Operator::Yok,
            yeni_sayi_mi: true,
        }
    }
}

impl eframe::App for HesapMakinesi {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Rust Hesap Makinesi");
            ui.add_space(10.0);

            // Ekrandaki sayıyı gösteren alan
            ui.label(egui::RichText::new(&self.ekran).size(40.0));
            ui.add_space(20.0);

            // Buton Izgarası
            egui::Grid::new("calculator_grid")
                .spacing([15.0, 15.0])
                .show(ui, |ui| {
                    // 1. Satır
                    if ui.button(egui::RichText::new("7").size(24.0)).clicked() { self.rakam_ekle("7"); }
                    if ui.button(egui::RichText::new("8").size(24.0)).clicked() { self.rakam_ekle("8"); }
                    if ui.button(egui::RichText::new("9").size(24.0)).clicked() { self.rakam_ekle("9"); }
                    if ui.button(egui::RichText::new("+").size(24.0)).clicked() { self.operator_sec(Operator::Topla); }
                    ui.end_row();

                    // 2. Satır
                    if ui.button(egui::RichText::new("4").size(24.0)).clicked() { self.rakam_ekle("4"); }
                    if ui.button(egui::RichText::new("5").size(24.0)).clicked() { self.rakam_ekle("5"); }
                    if ui.button(egui::RichText::new("6").size(24.0)).clicked() { self.rakam_ekle("6"); }
                    if ui.button(egui::RichText::new("-").size(24.0)).clicked() { self.operator_sec(Operator::Cikar); }
                    ui.end_row();

                    // 3. Satır
                    if ui.button(egui::RichText::new("1").size(24.0)).clicked() { self.rakam_ekle("1"); }
                    if ui.button(egui::RichText::new("2").size(24.0)).clicked() { self.rakam_ekle("2"); }
                    if ui.button(egui::RichText::new("3").size(24.0)).clicked() { self.rakam_ekle("3"); }
                    if ui.button(egui::RichText::new("*").size(24.0)).clicked() { self.operator_sec(Operator::Carp); }
                    ui.end_row();

                    // 4. Satır
                    if ui.button(egui::RichText::new("C").size(24.0)).clicked() { self.temizle(); }
                    if ui.button(egui::RichText::new("0").size(24.0)).clicked() { self.rakam_ekle("0"); }
                    if ui.button(egui::RichText::new("=").size(24.0)).clicked() { self.hesapla(); }
                    if ui.button(egui::RichText::new("/").size(24.0)).clicked() { self.operator_sec(Operator::Bol); }
                    ui.end_row();
                });
        });
    }
}

impl HesapMakinesi {
    fn rakam_ekle(&mut self, rakam: &str) {
        // Eğer bir operatöre basıldıktan sonra ilk kez rakama basılıyorsa ekranı temizle
        if self.yeni_sayi_mi {
            self.ekran = rakam.to_string();
            self.yeni_sayi_mi = false;
        } else if self.ekran == "0" {
            self.ekran = rakam.to_string();
        } else {
            self.ekran.push_str(rakam);
        }
    }

    fn operator_sec(&mut self, op: Operator) {
        // Ekrandaki mevcut yazıyı sayıya (f64) dönüştürüp hafızaya alıyoruz
        if let Ok(sayi) = self.ekran.parse::<f64>() {
            self.onceki_sayi = sayi;
            self.aktif_operator = op;
            self.yeni_sayi_mi = true; // Bir sonraki rakam basılışında ekran sıfırlansın
        }
    }

    fn hesapla(&mut self) {
        if self.aktif_operator == Operator::Yok {
            return;
        }

        // Ekrandaki ikinci sayıyı alıyoruz
        if let Ok(su_anki_sayi) = self.ekran.parse::<f64>() {
            let sonuc = match self.aktif_operator {
                Operator::Topla => self.onceki_sayi + su_anki_sayi,
                Operator::Cikar => self.onceki_sayi - su_anki_sayi,
                Operator::Carp => self.onceki_sayi * su_anki_sayi,
                Operator::Bol => {
                    if su_anki_sayi == 0.0 {
                        self.ekran = "Hata (0'a Bolme)".to_string();
                        self.aktif_operator = Operator::Yok;
                        self.yeni_sayi_mi = true;
                        return;
                    }
                    self.onceki_sayi / su_anki_sayi
                }
                Operator::Yok => su_anki_sayi,
            };

            // Sonucu ekrana yazdır ve durumları sıfırla
            self.ekran = sonuc.to_string();
            self.aktif_operator = Operator::Yok;
            self.yeni_sayi_mi = true;
        }
    }

    fn temizle(&mut self) {
        self.ekran = "0".to_string();
        self.onceki_sayi = 0.0;
        self.aktif_operator = Operator::Yok;
        self.yeni_sayi_mi = true;
    }
}
