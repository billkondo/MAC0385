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
        heap.insert(Certificate(3, 7))
        self.assertEqual(heap.delete_min(), Certificate(2, 0))
        self.assertEqual(heap.delete_min(), Certificate(2, 5))
        self.assertEqual(heap.delete_min(), Certificate(3, 4))
        self.assertEqual(heap.delete_min(), Certificate(3, 7))
        self.assertEqual(heap.delete_min(), Certificate(10, 2))
        self.assertTrue(heap.empty())

    def test_update_certificates_heap(self):
        heap = CertificatesHeap()

        heap.insert(Certificate(2, 5))
        heap.insert(Certificate(2, 0))
        heap.insert(Certificate(3, 4))
        heap.insert(Certificate(3, 7))
        heap.insert(Certificate(10, 2))

        self.assertEqual(heap.min(), Certificate(2, 0))
        heap.update(Certificate(20, 0))
        self.assertEqual(heap.min(), Certificate(2, 5))
        heap.update(Certificate(1, 7))
        self.assertEqual(heap.min(), Certificate(1, 7))
        heap.update(Certificate(0, 4))
        self.assertEqual(heap.min(), Certificate(0, 4))

    def test_delete_certificates_heap(self):
        heap = CertificatesHeap()

        heap.insert(Certificate(5, 0))
        heap.insert(Certificate(4, 1))
        heap.insert(Certificate(3, 2))
        heap.insert(Certificate(2, 3))
        heap.insert(Certificate(1, 4))

        self.assertEqual(heap.min(), Certificate(1, 4))
        heap.delete(3)
        heap.delete_min()
        self.assertEqual(heap.min(), Certificate(3, 2))
