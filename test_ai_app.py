"""
Tests for the AI application
These tests verify the application structure and logic,
without downloading actual models.
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os

# Import the ai_app module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ai_app import HuggingFaceAI


class TestHuggingFaceAI(unittest.TestCase):
    """AI application unit tests"""
    
    def setUp(self):
        """Test setup - create AI object"""
        self.ai = HuggingFaceAI()
    
    def test_initialization(self):
        """Test that the AI object initializes correctly"""
        self.assertIsNone(self.ai.sentiment_analyzer)
        self.assertIsNone(self.ai.qa_model)
        self.assertIsNone(self.ai.image_classifier)
        self.assertIsNone(self.ai.summarizer)
        self.assertIsNone(self.ai.image_captioner)
        self.assertIsNone(self.ai.story_generator)
    
    @patch('ai_app.pipeline')
    def test_load_sentiment_analyzer(self, mock_pipeline):
        """Test loading the sentiment analyzer"""
        mock_pipeline.return_value = Mock()
        self.ai.load_sentiment_analyzer()
        self.assertIsNotNone(self.ai.sentiment_analyzer)
        mock_pipeline.assert_called_once_with("sentiment-analysis")
    
    @patch('ai_app.pipeline')
    def test_load_qa_model(self, mock_pipeline):
        """Test loading the QA model"""
        mock_pipeline.return_value = Mock()
        self.ai.load_qa_model()
        self.assertIsNotNone(self.ai.qa_model)
        mock_pipeline.assert_called_once_with("question-answering")
    
    @patch('ai_app.pipeline')
    def test_load_summarizer(self, mock_pipeline):
        """Test loading the summarizer"""
        mock_pipeline.return_value = Mock()
        self.ai.load_summarizer()
        self.assertIsNotNone(self.ai.summarizer)
        mock_pipeline.assert_called_once_with("summarization", model="facebook/bart-large-cnn")
    
    @patch('ai_app.pipeline')
    def test_load_image_classifier(self, mock_pipeline):
        """Test loading the image classifier"""
        mock_pipeline.return_value = Mock()
        self.ai.load_image_classifier()
        self.assertIsNotNone(self.ai.image_classifier)
        mock_pipeline.assert_called_once_with("image-classification")
    
    @patch('ai_app.pipeline')
    def test_load_image_captioner(self, mock_pipeline):
        """Test loading the image captioner (BLIP)"""
        mock_pipeline.return_value = Mock()
        self.ai.load_image_captioner()
        self.assertIsNotNone(self.ai.image_captioner)
        mock_pipeline.assert_called_once_with("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    @patch('ai_app.pipeline')
    def test_load_story_generator(self, mock_pipeline):
        """Test loading the story generator"""
        mock_pipeline.return_value = Mock()
        self.ai.load_story_generator()
        self.assertIsNotNone(self.ai.story_generator)
        mock_pipeline.assert_called_once_with("text-generation", model="gpt2")
    
    @patch('ai_app.pipeline')
    def test_analyze_sentiment(self, mock_pipeline):
        """Test the sentiment analysis function"""
        # Mock pipeline setup
        mock_analyzer = Mock()
        mock_analyzer.return_value = [{'label': 'POSITIVE', 'score': 0.99}]
        mock_pipeline.return_value = mock_analyzer
        
        # Execute sentiment analysis
        result = self.ai.analyze_sentiment("Great product!")
        
        # Assertions
        self.assertEqual(result['label'], 'POSITIVE')
        self.assertEqual(result['score'], 0.99)
        mock_analyzer.assert_called_once_with("Great product!")
    
    @patch('ai_app.pipeline')
    def test_answer_question(self, mock_pipeline):
        """Test the question answering function"""
        # Mock QA model
        mock_qa = Mock()
        mock_qa.return_value = {
            'answer': '2016',
            'score': 0.98
        }
        mock_pipeline.return_value = mock_qa
        
        # Execute question-answer
        context = "The company was founded in 2016."
        question = "When was the company founded?"
        result = self.ai.answer_question(context, question)
        
        # Assertions
        self.assertEqual(result['answer'], '2016')
        self.assertEqual(result['score'], 0.98)
        mock_qa.assert_called_once_with(question=question, context=context)
    
    @patch('ai_app.pipeline')
    def test_summarize_text(self, mock_pipeline):
        """Test the text summarization function"""
        # Mock summarizer
        mock_summ = Mock()
        mock_summ.return_value = [{'summary_text': 'Short summary'}]
        mock_pipeline.return_value = mock_summ
        
        # Execute summarization
        text = "This is a very long text that needs to be summarized."
        result = self.ai.summarize_text(text)
        
        # Assertions
        self.assertEqual(result, 'Short summary')
        mock_summ.assert_called_once()
    
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_classify_image_local(self, mock_pipeline, mock_image):
        """Test image classification with local file"""
        # Mock image classifier
        mock_classifier = Mock()
        mock_classifier.return_value = [
            {'label': 'cat', 'score': 0.95},
            {'label': 'dog', 'score': 0.03}
        ]
        mock_pipeline.return_value = mock_classifier
        
        # Mock image loading
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Execute image classification
        results = self.ai.classify_image("test_image.jpg")
        
        # Assertions
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['label'], 'cat')
        self.assertEqual(results[0]['score'], 0.95)
        mock_image.open.assert_called_once_with("test_image.jpg")
    
    @patch('ai_app.requests')
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_classify_image_url(self, mock_pipeline, mock_image, mock_requests):
        """Test image classification from URL"""
        # Mock image classifier
        mock_classifier = Mock()
        mock_classifier.return_value = [{'label': 'car', 'score': 0.88}]
        mock_pipeline.return_value = mock_classifier
        
        # Mock HTTP request
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_requests.get.return_value = mock_response
        
        # Mock image loading
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Execute image classification with URL
        results = self.ai.classify_image("http://example.com/car.jpg")
        
        # Assertions
        self.assertEqual(results[0]['label'], 'car')
        mock_requests.get.assert_called_once_with("http://example.com/car.jpg", timeout=10)
    
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_caption_image_local(self, mock_pipeline, mock_image):
        """Test image captioning with local file"""
        # Mock image captioner
        mock_captioner = Mock()
        mock_captioner.return_value = [{'generated_text': 'a cat sitting on a couch'}]
        mock_pipeline.return_value = mock_captioner
        
        # Mock image loading
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Execute image captioning
        caption = self.ai.caption_image("test_image.jpg")
        
        # Assertions
        self.assertEqual(caption, 'a cat sitting on a couch')
        mock_image.open.assert_called_once_with("test_image.jpg")
    
    @patch('ai_app.pipeline')
    def test_generate_story(self, mock_pipeline):
        """Test story generation from image description"""
        # Mock story generator
        mock_generator = Mock()
        mock_generator.return_value = [{'generated_text': 'Once upon a time, there was a happy cat who lived in a cozy house.'}]
        mock_pipeline.return_value = mock_generator
        
        # Execute story generation
        story = self.ai.generate_story("a cat sitting on a couch")
        
        # Assertions
        self.assertIn("Once upon a time", story)
        mock_generator.assert_called_once()
    
    @patch('ai_app.Image')
    @patch('ai_app.pipeline')
    def test_image_to_story(self, mock_pipeline, mock_image):
        """Test the complete image to story pipeline"""
        # Mock captioner and generator
        mock_captioner = Mock()
        mock_captioner.return_value = [{'generated_text': 'a happy dog playing in the park'}]
        
        mock_generator = Mock()
        mock_generator.return_value = [{'generated_text': 'Once upon a time, a happy dog was playing in the park.'}]
        
        # Return different mocks for different pipeline calls
        mock_pipeline.side_effect = [mock_captioner, mock_generator]
        
        # Mock image loading
        mock_img = Mock()
        mock_image.open.return_value = mock_img
        
        # Execute image to story
        result = self.ai.image_to_story("test_image.jpg")
        
        # Assertions
        self.assertIn('caption', result)
        self.assertIn('story', result)
        self.assertEqual(result['caption'], 'a happy dog playing in the park')


class TestApplicationStructure(unittest.TestCase):
    """Application structure tests"""
    
    def test_huggingface_class_exists(self):
        """Check that the HuggingFaceAI class exists with all methods"""
        self.assertTrue(hasattr(HuggingFaceAI, 'load_sentiment_analyzer'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_qa_model'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_summarizer'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_image_classifier'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_image_captioner'))
        self.assertTrue(hasattr(HuggingFaceAI, 'load_story_generator'))
        self.assertTrue(hasattr(HuggingFaceAI, 'analyze_sentiment'))
        self.assertTrue(hasattr(HuggingFaceAI, 'answer_question'))
        self.assertTrue(hasattr(HuggingFaceAI, 'summarize_text'))
        self.assertTrue(hasattr(HuggingFaceAI, 'classify_image'))
        self.assertTrue(hasattr(HuggingFaceAI, 'caption_image'))
        self.assertTrue(hasattr(HuggingFaceAI, 'generate_story'))
        self.assertTrue(hasattr(HuggingFaceAI, 'image_to_story'))
    
    def test_class_instantiation(self):
        """Check that the class can be instantiated"""
        ai = HuggingFaceAI()
        self.assertIsInstance(ai, HuggingFaceAI)


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
