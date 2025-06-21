import unittest
from unittest.mock import MagicMock, patch


from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.model.Corso import Corso
from GestioneClienti.model.Abbonamento import Abbonamento
from GestioneClienti.model.Cliente import Cliente

class ClienteControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Creazione del finto Dao
        patcher = patch('GestioneClienti.controller.cliente_controller.ClienteDaoFirebase')

        self.addCleanup(patcher.stop) # pulizia della patch automatica quando finiscono i test
        # oggetto mock che rappresenta il dao
        self.mock_dao_class = patcher.start()
        # l'istanza mock del Dao che il controller utilizzerà (viene creata dinamicamente quando effettivamente viene istanziata)
        self.mock_dao = self.mock_dao_class.return_value

        # Creazione della finta view
        self.view = MagicMock()
        self.view.visualizzaClienti = MagicMock()

        # Inizializzazione del controller
        self.controller = ClienteController(self.view)

    def test_aggiungi_cliente_success(self):
        nuovoCliente = Cliente(
            id='50',
            nome='Mario', 
            cognome='Rossi', 
            sesso= 'Maschio',
            telefono= '3292098383',
            email='mariettino@esempio.com',
            data_nascita='06/05/2002',
            certificatoMedico=True
            )
        self.mock_dao.aggiungi_cliente.return_value = True

        result = self.controller.aggiungi_cliente(nuovoCliente)
        
        # view -> form e bottone "salva cliente"
        # controller -> self.controller.aggiungi_cliente(nuovoCliente)
        # dao -> self.dao.aggiungi_cliente(nuovoCliente) [boolean: True o False] OGGETTO FALSO
        # database(firebase)

        self.assertTrue(result)
        self.mock_dao.aggiungi_cliente.assert_called_once_with(nuovoCliente)
    
    def test_aggiungi_cliente_failure_email_esistente(self):
        cliente = Cliente(
            id='69', 
            nome='Luigi', 
            cognome='Verdi', 
            sesso='Maschio',
            telefono='3281234567', 
            email='marietto@esempio.com',
            data_nascita='01/01/1990', 
            certificatoMedico=False
            )
        
        self.mock_dao.aggiungi_cliente.return_value = False

        result = self.controller.aggiungi_cliente(cliente)

        self.assertFalse(result)
        self.mock_dao.aggiungi_cliente.assert_called_once_with(cliente)
    
    def test_elimina_cliente_success(self):
        self.mock_dao.elimina_cliente.return_value = True

        result = self.controller.elimina_cliente('2')

        self.assertTrue(result)
        self.mock_dao.elimina_cliente.assert_called_once_with('2')
        self.view.visualizzaClienti.assert_called()  # ricarico lista

    def test_elimina_cliente_failure(self):
        self.mock_dao.elimina_cliente.return_value = False

        result = self.controller.elimina_cliente('5')

        self.assertFalse(result)
        self.mock_dao.elimina_cliente.assert_called_once_with('5')
    
    def test_trova_cliente_by_nome_trovato(self):
        expected = [    Cliente(id='1', 
                            nome='Anna', 
                            cognome='Bianchi', 
                            sesso='Femmina',
                            telefono='333111222', 
                            email='anna@esempio.com',
                            data_nascita='02/02/1985', 
                            certificatoMedico=True
                        ),
                        Cliente(id='6', 
                            nome='Anna', 
                            cognome='Neri', 
                            sesso='Femmina',
                            telefono='3298765373', 
                            email='annaneri@esempio.com',
                            data_nascita='02/05/1983', 
                            certificatoMedico=True
                        )
                    ]
        self.mock_dao.trova_cliente_by_nome.return_value = expected

        result = self.controller.trova_cliente_by_nome('Anna')

        self.assertEqual(result, expected)
        self.mock_dao.trova_cliente_by_nome.assert_called_once_with('Anna')
    
    def test_trova_cliente_by_nome_non_trovato(self):
        self.mock_dao.trova_cliente_by_nome.return_value = []

        result = self.controller.trova_cliente_by_nome('Alessandro')

        self.assertEqual(result, [])
    
    def test_add_abbonamento_to_cliente_success(self):

        cliente_id = '50'
        nuovoAbbonamento = Abbonamento(
            id='1',
            corso='pilates',
            data_inizio = '20/06/2025',
            data_fine='20/07/2025',
            prezzo=60.00,
            saldato=True,
            stato='Attivo'
        )

        self.mock_dao.add_abbonamento_to_cliente.return_value = True
        result = self.controller.add_abbonamento_to_cliente(cliente_id, nuovoAbbonamento)

        self.assertTrue(result)
        self.mock_dao.add_abbonamento_to_cliente.assert_called_once_with(cliente_id, nuovoAbbonamento)

    def test_elimina_abbonamento_success(self):

        abbonamento_id = '1'

        self.mock_dao.elimina_abbonamento.return_value = True
        result = self.controller.elimina_abbonamento('1')

        self.assertTrue(result)
        self.mock_dao.elimina_abbonamento.assert_called_once_with(abbonamento_id)

    def test_get_all_corsi_success(self):
        expected = [
            Corso(
                id = '1',
                nome= 'Boxe',
                descrizione = 'corso per principianti di boxe.',
                durata_mesi = 3,
                prezzo = 90.00,
                pt_assegnati= 'pt1'
            ),
            Corso(
                id = '2',
                nome= 'pilates',
                descrizione = 'corso per principianti di boxe.',
                durata_mesi = 3,
                prezzo = 90.00,
                pt_assegnati= 'pt2'
            )
        ]

        self.mock_dao.get_all_corsi.return_value = expected

        result = self.controller.get_all_corsi()

        self.assertEqual(result, expected)

    def test_get_abbonamenti_by_cliente_id_success(self):
        cliente_id = '2'

        expected = [
            Abbonamento(
                id='1',
                id_cliente = '2',
                corso='pilates',
                data_inizio = '20/06/2025',
                data_fine='20/07/2025',
                prezzo=60.00,
                saldato=True,
                stato='Attivo'
            )
        ]
        self.mock_dao.get_abbonamenti_by_cliente_id.return_value = expected

        result = self.controller.get_abbonamenti_by_cliente_id(cliente_id)
        self.assertEqual(result, expected)
    
    def test_modifica_cliente_success(self):

        clienteAggiornato = Cliente(id='1', 
                            nome='Anna Maria', 
                            cognome='Bianchi', 
                            sesso='Femmina',
                            telefono='333111222', 
                            email='anna@esempio.com',
                            data_nascita='02/02/1985', 
                            certificatoMedico=True
                        )
        self.mock_dao.update_cliente.return_value = True
        
        result = self.controller.modifica_cliente(clienteAggiornato)

        self.assertTrue(result)
        self.mock_dao.update_cliente.assert_called_once_with(clienteAggiornato)

    def test_modifica_cliente_failure(self):

        clienteAggiornato = Cliente(id='1', 
                            nome='Anna Maria', 
                            cognome='Bianchi', 
                            sesso='Femmina',
                            telefono='333111222', 
                            email='anna@esempio.com',
                            data_nascita='02/029/1985', 
                            certificatoMedico=True
                        )
        self.mock_dao.update_cliente.return_value = False
        
        result = self.controller.modifica_cliente(clienteAggiornato)

        self.assertFalse(result)
        self.mock_dao.update_cliente.assert_called_once_with(clienteAggiornato)

if __name__ == '__main__':
    unittest.main()

