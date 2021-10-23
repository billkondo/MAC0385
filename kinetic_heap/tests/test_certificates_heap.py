import unittest

from kinetic_heap import Certificate, CertificatesHeap


class TestCertificatesHeap(unittest.TestCase):
    def test_certificates_heap(self):
        heap = CertificatesHeap()

        heap.insert(Certificate(2, 5))
        self.assertFalse(heap.empty())

        self.assertEqual(heap.min(), Certificate(2, 5))
        heap.insert(Certificate(2, 0))
        self.assertEqual(heap.min(), Certificate(2, 0))
        heap.insert(Certificate(3, 4))
        heap.insert(Certificate(10, 2))
        heap.insert(Certificate(3, 5))
        self.assertEqual(heap.delete_min(), Certificate(2, 0))
        self.assertEqual(heap.delete_min(), Certificate(2, 5))
        self.assertEqual(heap.delete_min(), Certificate(3, 4))
        self.assertEqual(heap.delete_min(), Certificate(3, 5))
        self.assertEqual(heap.delete_min(), Certificate(10, 2))
        self.assertTrue(heap.empty())

    def test_update_certificates_heap(self):
        heap = CertificatesHeap()

        heap.insert(Certificate(2, 5))
        heap.insert(Certificate(2, 0))
        heap.insert(Certificate(3, 4))
        heap.insert(Certificate(3, 5))
        heap.insert(Certificate(10, 2))

        self.assertEqual(heap.min(), Certificate(2, 0))
        heap.update(0, Certificate(20, 10))
        self.assertEqual(heap.min(), Certificate(2, 5))
        heap.update(2, Certificate(1, 1))
        self.assertEqual(heap.min(), Certificate(1, 1))
        heap.update(4, Certificate(0, 0))
        self.assertEqual(heap.min(), Certificate(0, 0))
