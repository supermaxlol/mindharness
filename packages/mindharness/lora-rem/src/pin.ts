/**
 * pin — adapter id is pinned in SelfModelService.
 * Promotion requires a CAS revision (N -> N+1) or it is rejected.
 * Prevents silent identity swap.
 */

export function pinnedAdapterRevision(oldAdapter: string | null, newAdapter: string, revision: number): number {
  if (oldAdapter === newAdapter) return revision;
  return revision + 1; // CAS bump required
}
