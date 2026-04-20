from datetime import datetime
import random


VACUNAS_BASE = [
    {
        "nombre": "BCG",
        "descripcion": "Vacuna contra la tuberculosis",
        "edad_recomendada": "Recien nacido",
        "dosis_requeridas": 1,
        "intervalo_dosis_rango": (0, 0),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Hepatitis B",
        "descripcion": "Vacuna contra el virus de la hepatitis B",
        "edad_recomendada": "0-2 meses",
        "dosis_requeridas": 3,
        "intervalo_dosis_rango": (28, 35),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Pentavalente",
        "descripcion": "Vacuna contra difteria, tetanos, pertussis, hepatitis B y Hib",
        "edad_recomendada": "2-6 meses",
        "dosis_requeridas": 3,
        "intervalo_dosis_rango": (56, 65),
        "requiere_refuerzo": True,
    },
    {
        "nombre": "Polio IPV",
        "descripcion": "Vacuna inactivada contra la poliomielitis",
        "edad_recomendada": "2-6 meses",
        "dosis_requeridas": 3,
        "intervalo_dosis_rango": (56, 65),
        "requiere_refuerzo": True,
    },
    {
        "nombre": "Rotavirus",
        "descripcion": "Vacuna contra el rotavirus causante de diarrea grave",
        "edad_recomendada": "2-4 meses",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (56, 65),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Neumococo",
        "descripcion": "Vacuna contra el Streptococcus pneumoniae",
        "edad_recomendada": "2-12 meses",
        "dosis_requeridas": 3,
        "intervalo_dosis_rango": (56, 65),
        "requiere_refuerzo": True,
    },
    {
        "nombre": "Influenza",
        "descripcion": "Vacuna contra la influenza estacional",
        "edad_recomendada": "6 meses en adelante",
        "dosis_requeridas": 1,
        "intervalo_dosis_rango": (360, 370),
        "requiere_refuerzo": True,
    },
    {
        "nombre": "Triple Viral SRP",
        "descripcion": "Vacuna contra sarampion, rubeola y paperas",
        "edad_recomendada": "12-15 meses",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (1800, 1830),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Varicela",
        "descripcion": "Vacuna contra el virus varicela-zoster",
        "edad_recomendada": "12-15 meses",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (1080, 1110),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Fiebre Amarilla",
        "descripcion": "Vacuna contra el virus de la fiebre amarilla",
        "edad_recomendada": "12 meses en adelante",
        "dosis_requeridas": 1,
        "intervalo_dosis_rango": (0, 0),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "Hepatitis A",
        "descripcion": "Vacuna contra el virus de la hepatitis A",
        "edad_recomendada": "12-23 meses",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (168, 195),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "DPT",
        "descripcion": "Refuerzo contra difteria, pertussis y tetanos",
        "edad_recomendada": "18 meses",
        "dosis_requeridas": 1,
        "intervalo_dosis_rango": (0, 0),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "VPH",
        "descripcion": "Vacuna contra el virus del papiloma humano",
        "edad_recomendada": "9-14 anos",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (168, 195),
        "requiere_refuerzo": False,
    },
    {
        "nombre": "COVID-19",
        "descripcion": "Vacuna contra el SARS-CoV-2",
        "edad_recomendada": "12 anos en adelante",
        "dosis_requeridas": 2,
        "intervalo_dosis_rango": (21, 28),
        "requiere_refuerzo": True,
    },
    {
        "nombre": "Meningococo",
        "descripcion": "Vacuna contra la enfermedad meningococica invasiva",
        "edad_recomendada": "11-12 anos",
        "dosis_requeridas": 1,
        "intervalo_dosis_rango": (0, 0),
        "requiere_refuerzo": True,
    },
]


def simular_vacunas_catalogo():
    """
    Simula datos para la tabla VACUNAS_CATALOGO.

    Returns:
        list: Lista de diccionarios con datos de vacunas del catalogo.
    """
    catalogo = []

    for idx, vacuna in enumerate(VACUNAS_BASE, start=1):
        rango = vacuna["intervalo_dosis_rango"]
        intervalo = random.randint(rango[0], rango[1]) if rango[0] != rango[1] else rango[0]

        registro = {
            "id_vacuna": idx,
            "nombre_vacuna": vacuna["nombre"],
            "descripcion": vacuna["descripcion"],
            "edad_recomendada": vacuna["edad_recomendada"],
            "dosis_requeridas": vacuna["dosis_requeridas"],
            "intervalo_dosis_dias": intervalo,
            "requiere_refuerzo": vacuna["requiere_refuerzo"],
        }
        catalogo.append(registro)

    return catalogo