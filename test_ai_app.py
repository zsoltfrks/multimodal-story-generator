"""
Tesztek az AI alkalmazáshoz
Ezek a tesztek az alkalmazás struktúráját és logikáját ellenőrzik,
anélkül hogy tényleges modelleket töltenének le.
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os

# Importáljuk az ai_app modult
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ai_app import HuggingFaceAI


class TestHuggingFaceAI(unittest.TestCase):
    """AI alkalmazás unit tesztek"""
    
    def setUp(self):
        """Test setup - AI objektum létrehozása"""
        self.ai = HuggingFaceAI()
    
    def test_initialization(self):
        """Teszteli, hogy az AI objektum helyesen inicializálódik"""
        self.assertIsNone(self.ai.sentiment_analyzer)
        self.assertIsNone(self.ai.qa_model)
        self.assertIsNone(self.ai.image_classifier)
        self.assertIsNone(self.ai.summarizer)
    
    @patch('ai_app.pipeline')
    def test_load_sentiment_analyzer(self, mock_pipeline):
        """Teszteli a sentiment analyzer betöltését"""
        mock_pipeline.return_value = Mock()
        self.ai.load_sentiment_analyzer()
        self.assertIsNotNone(self.ai.sentiment_analyzer)
        mock_pipeline.assert_called_once_with("sentiment-analysis")
    
    @patch('ai_app.pipeline')
    def test_load_qa_model(self, mock_pipeline):
        """Teszteli a QA modell betöltését"""
        mock_pipeline.return_value = Mock()
        self.ai.load_qa_model()
        self.assertIsNotNone(self.ai.qa_model)
        mock_pipeline.assert_called_once_with("question-answering")
    
    @patch('ai_app.pipeline')
    def test_load_summarizer(self, mock_pipeline):
        """Teszteli a summarizer betöltését"""
        mock_pipeline.return_value = Mock()
        self.ai.load_summarizer()
        self.assertIsNotNone(self.ai.summarizer)
        mock_pipeline.assert_called_once_with("summarization", model="facebook/bart-large-cnn")
    
    @patch('ai_app.pipeline')
    def test_load_image_classifier(self, mock_pipeline):
        """Teszteli az image classifier betöltését"""
        mock_pipeline.return_value = Mock()
        self.ai.load_image_classifier()
        self.assertIsNotNone(self.ai.image_classifier)
        mock_pipeline.assert_called_once_with("image-classification")
    
    @patch('ai_app.pipeline')
    def test_analyze_sentiment(self, mock_pipeline):
        """Teszteli a sentiment analysis funkciót"""
        # Mock pipeline beállítása
        mock_analyzer = Mock()
        mock_analyzer.return_value = [{'label': 'POSITIVE', 'score': 0.99}]
        mock_pipeline.return_value = mock_analyzer
        
        # Sentiment elemzés végrehajtása
        result = self.ai.analyze_sentiment("Great product!")
        
        # Ellenőrzések
        self.assertEqual(result['label'], 'POSITIVE')
        self.assertEqual(result['score'], 0.99)
        mock_analyzer.assert_called_once_with("Great product!")
    
    @patch('ai_app.pipeline')
    def test_answer_question(self, mock_pipeline):
        """Teszteli a question answering funkciót"""
        # Mock QA modell
        mock_qa = Mock()
        mock_qa.return_value = {
            'answer': '2016',
            'score': 0.98
        }
        mock_pipeline.return_value = mock_qa
        
        # Kérdés-válasz végrehajtása
        context = "The company was founded in 2016."
        question = "When was the company founded?"
        result = self.ai.answer_question(context, question)
        
        # Ellenőrzések
        self.assertEqual(result['answer'], '2016')
        self.assertEqual(result['score'], 0.98)
        mock_qa.assert_called_once_with(question=question, context=context)
    
    @patch('ai_app.pipeline')
    def test_summarize_text(self, mock_pipeline):
        """Teszteli a text summarization funkciót"""
        # Mock summarizer
        mock_summ = Mock()
        mock_summ.return_value = [{'summary_text': 'Short summary'}]
        mock_pipeline.return_value = mock_summ
        
        # Összefoglalás végrehajtása
        text = "This is a very long text that needs to be summarized."
        result = self.ai.summarize_text(text)
        
        # Ellenőrzések
        self.assertEqual(result, 'Short summary')
        mock_summ.assert_called_once()
    
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_classify_image_local(self, mock_pipeline, mock_image):
        """Teszteli a képosztályozást lokális fájllal"""
        # Mock image classifier
        mock_classifier = Mock()
        mock_classifier.return_value = [
            {'label': 'cat', 'score': 0.95},
            {'label': 'dog', 'score': 0.03}
        ]
        mock_pipeline.return_value = mock_classifier
        
        # Mock kép betöltés
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Képosztályozás végrehajtása
        results = self.ai.classify_image("test_image.jpg")
        
        # Ellenőrzések
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['label'], 'cat')
        self.assertEqual(results[0]['score'], 0.95)
        mock_image.open.assert_called_once_with("test_image.jpg")
    
    @patch('ai_app.requests')
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_classify_image_url(self, mock_pipeline, mock_image, mock_requests):
        """Teszteli a képosztályozást URL-ről"""
        # Mock image classifier
        mock_classifier = Mock()
        mock_classifier.return_value = [{'label': 'car', 'score': 0.88}]
        mock_pipeline.return_value = mock_classifier
        
        # Mock HTTP kérés
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_requests.get.return_value = mock_response
        
        # Mock kép betöltés
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Képosztályozás végrehajtása URL-lel
        results = self.ai.classify_image("http://example.com/car.jpg")
        
        # Ellenőrzések
        self.assertEqual(results[0]['label'], 'car')
        mock_requests.get.assert_called_once_with("http://example.com/car.jpg")


class TestApplicationStructure(unittest.TestCase):
    """Alkalmazás struktúra tesztek"""
    
    def test_huggingface_class_exists(self):
        """Ellenőrzi, hogy a HuggingFaceAI osztály létezik"""
        self.assertTrue(hasattr(HuggingFaceAI, 'load_sentiment_analyzer'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_qa_model'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_summarizer'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_image_classifier'))
        self.assertTrue(hasattr(HuggingFaceAI, 'analyze_sentiment'))
        self.assertTrue(hasattr(HuggingFaceAI, 'answer_question'))
        self.assertTrue(hasattr(HuggingFaceAI, 'summarize_text'))
        self.assertTrue(hasattr(HuggingFaceAI, 'classify_image'))
    
    def test_class_instantiation(self):
        """Ellenőrzi, hogy az osztály példányosítható"""
        ai = HuggingFaceAI()
        self.assertIsInstance(ai, HuggingFaceAI)


if __name__ == '__main__':
    # Tesztek futtatása
    unittest.main(verbosity=2)
