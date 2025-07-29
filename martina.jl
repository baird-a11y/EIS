using GLMakie
using Statistics
using GeophysicalModelGenerator
using GMT
using DataFrames

Topo = import_topo([28.2, 30.4, 96.4 ,99.1], file="@earth_relief_01m")

# Rest deines Codes bleibt gleich
x = Topo.lon.val[:,1]
y = Topo.lat.val[1,:]
data_heatmap = ustrip(Topo.fields.topography[:,:,1])
fig, ax, hm = heatmap(x,y,data_heatmap)




using GeophysicalModelGenerator, GMT
Topo = import_topo([4,20,37,49], file="@earth_relief_01m")



using Pkg
Pkg.status("GMT")



using GMT

function test_gmt_installation()
    println("=== GMT Installation Test ===")
    
    # Test 1: GMT laden
    try
        println("1. GMT Package laden...")
        # GMT ist bereits geladen
        println("✅ GMT Package erfolgreich geladen")
    catch e
        println("❌ GMT Package Fehler: $e")
        return false
    end
    
    # Test 2: GMT Version
    try
        println("2. GMT Version prüfen...")
        version_info = gmt("--version")
        println("✅ GMT Version: $(version_info)")
    catch e
        println("❌ GMT Version Fehler: $e")
        return false
    end
    
    # Test 3: Einfache GMT Funktion
    try
        println("3. Einfache GMT Funktion testen...")
        # Erstelle einfache Daten
        data = [0 0; 1 1; 2 4]
        result = gmt("psxy -R0/2/0/4 -JX3i -P", data)
        println("✅ GMT Plotting funktioniert")
    catch e
        println("❌ GMT Plotting Fehler: $e")
        return false
    end
    
    # Test 4: Daten Download Test (kleiner Bereich)
    try
        println("4. GMT Daten Download testen...")
        # Sehr kleiner Bereich für schnellen Test
        small_data = gmt("grdcut @earth_relief_60m -R0/1/0/1")
        println("✅ GMT Daten Download funktioniert")
    catch e
        println("❌ GMT Daten Download Fehler: $e")
        println("   Das könnte ein Netzwerk-Problem sein")
        return false
    end
    
    println("=== Alle Tests bestanden! ===")
    return true
end

# Tests ausführen
test_gmt_installation()


using Pkg

# GMT_jll explizit installieren
Pkg.add("GMT_jll")

# GMT neu installieren
Pkg.rm("GMT")
Pkg.add("GMT")

# Package Cache leeren
Pkg.gc()

# Neu starten von Julia erforderlich!

using Pkg

# Alle GMT-verwandten Pakete entfernen
try Pkg.rm("GMT") catch end
try Pkg.rm("GMT_jll") catch end
try Pkg.rm("GeophysicalModelGenerator") catch end

# Registry aktualisieren
Pkg.update()

# Neu installieren
Pkg.add("GMT_jll")  # Zuerst die C-Bibliothek
Pkg.add("GMT")      # Dann das Julia Interface
Pkg.add("GeophysicalModelGenerator")  # Dann dein Hauptpaket

# Julia neu starten!

using Pkg

# 1. Artifacts Cache komplett leeren
println("Lösche Artifacts Cache...")
try
    rm(joinpath(first(DEPOT_PATH), "artifacts"), recursive=true, force=true)
    println("✅ Artifacts Cache gelöscht")
catch e
    println("⚠️ Artifacts Cache konnte nicht gelöscht werden: $e")
end

# 2. Compiled Cache leeren
try
    rm(joinpath(first(DEPOT_PATH), "compiled"), recursive=true, force=true)
    println("✅ Compiled Cache gelöscht")
catch e
    println("⚠️ Compiled Cache konnte nicht gelöscht werden: $e")
end

# 3. Julia neu starten erforderlich!
exit()


using Pkg

# Pakete neu installieren (lädt Artifacts neu herunter)
Pkg.add("PROJ_jll")
Pkg.add("GMT_jll") 
Pkg.add("GMT")